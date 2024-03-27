import traceback
import requests
import zipfile
import io
import os
from datetime import datetime
import glob
import importlib.util
import sys

def get_test_cases(url):
    # Send a GET request to the URL to download the zip file
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get today's date
        current_date = datetime.now().strftime("%Y_%m_%d")

        # Find the most recent "long problems" directory
        long_problems_dirs = sorted(glob.glob("*Long_Problems"), key=os.path.getmtime, reverse=True)
        most_recent_long_problems_dir = long_problems_dirs[0] if long_problems_dirs else current_date + "_Long_Problems"

        # Create a directory to save the extracted files
        extract_dir = os.path.join(most_recent_long_problems_dir, "test_cases")
        os.makedirs(extract_dir, exist_ok=True)

        # Open the zip file from the response content
        with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
            # Get a list of files in the zip file excluding those in the __MACOSX directory
            file_list = [file for file in zip_ref.namelist() if not file.startswith("__MACOSX")]

            # Extract and save the contents of the zip file 
            for file in sorted(file_list):
                if not file.endswith('/'):
                    # Determine the target subdirectory for test files based on file type
                    if 'test' in file.lower():
                        # Extract the program name from the file name
                        program_name = file.split("-")[2]
                        sub_dir_name = program_name
                        sub_dir_path = os.path.join("test_files", sub_dir_name)
                    else:
                        sub_dir_path = "text_files"

                    # Create a subdirectory for the file type if it doesn't already exist
                    target_dir = os.path.join(extract_dir, sub_dir_path)
                    os.makedirs(target_dir, exist_ok=True)

                    # Save the extracted file to the appropriate subdirectory
                    with zip_ref.open(file) as extracted_file:
                        contents = extracted_file.read()

                        file_path = os.path.join(target_dir, os.path.basename(file))
                        with open(file_path, 'wb') as output_file:
                            output_file.write(contents)
                        print(f"Saved file: {file_path}")

        print("Extraction and saving complete in the most recent Long Problems directory.")
    else:
        print("Failed to download the zip file. Status code: ", response.status_code)

def run_test_cases():
    # Find the most recent "Long Problems" directory
    current_date = datetime.now().strftime("%Y_%m_%d")
    long_problems_dirs = sorted(glob.glob("*Long_Problems"), key=os.path.getmtime, reverse=True)
    most_recent_long_problems_dir = long_problems_dirs[0] if long_problems_dirs else current_date + "_Long_Problems"

    # Navigate to the test_cases/test_files directory within the most recent "Long Problems" directory
    test_files_dir = os.path.join(most_recent_long_problems_dir, "test_cases", "test_files")
    os.makedirs(test_files_dir, exist_ok=True)

    for folder_name in os.listdir(test_files_dir):
        folder_path = os.path.join(test_files_dir, folder_name)
        if os.path.isdir(folder_path):
            try:
                program_path = os.path.join(most_recent_long_problems_dir, f"{folder_name}.py")
                module_name = os.path.splitext(os.path.basename(program_path))[0]

                # Load the module from the provided script path
                spec = importlib.util.spec_from_file_location(module_name, program_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Call the main function from the loaded module
                try:
                    module_folder = os.path.join(test_files_dir, module.__name__)

                    if os.path.exists(module_folder) and os.path.isdir(module_folder):
                        for root, _, files in os.walk(module_folder):
                            for file in files:
                                if file.endswith(".stdin"):
                                    file_path = os.path.join(root, file)
                                    out_file_path = os.path.splitext(file_path)[0] + ".out"

                                    try:
                                        # Read the expected output from the .out file
                                        with open(out_file_path, 'r') as out_file:
                                            expected_output = out_file.read().strip()
                                        
                                        with open(file_path, 'r') as f:
                                            stdin_content = f.read()

                                        stdin_and_path = '/'.join(os.path.splitext(file_path)[0].split('/')[0:2]) + f'/text_files/{stdin_content}'
                                        # Redirect sys.stdin to use the contents of the .stdin file
                                        sys.stdin = io.StringIO(stdin_and_path)

                                        # Redirect sys.stdout to capture the output
                                        sys.stdout = io.StringIO()

                                        # Call the main function with the redirected input
                                        try:
                                            result = getattr(module, 'main', None)()
                                        except Exception as e:
                                            exc_type, exc_obj, tb = sys.exc_info()
                                            frame = tb.tb_frame
                                            line_number = traceback.extract_tb(tb)[-1].lineno
                                            file_name = frame.f_code.co_filename
                                            print(f"An error occurred at line {line_number} in {file_name}: {e}")


                                        # Get the output produced by the main function
                                        actual_output = sys.stdout.getvalue().strip()
                                        sys.stdout = sys.__stdout__

                                        # Compare the actual output with the expected output
                                        if actual_output == expected_output:
                                            print(f"✅ Test case {file} passed.")
                                        else:
                                            print(f"❌ Test case {file} failed. Expected output: {expected_output}, Actual output: {actual_output}")

                                    except Exception as e:
                                        print(f"Error processing test case {file}: {e}")

                except TypeError:
                    print(f"{module.__name__} does not have main() function")

            except ImportError as e:
                print(f"Error importing or executing main() from {folder_name}.py: {e}")

# if __name__ == "__main__":
#     get_or_run = input('get/run (g/r):\n')
#     if get_or_run == 'g':
#         url = input('URL:\n')
#         get_test_cases(url) 
#     if get_or_run == 'r':
#         run_test_cases()
#     else:
#         raise Exception('Invalid Input')

run_test_cases()

        
