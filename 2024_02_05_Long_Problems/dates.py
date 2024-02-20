"""
File: dates.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This code reads a file with dates and events, 
converts the dates to a canonical format, and handles 
inserting and reading dates/events. 
"""
def canonicalize_date(date_str):
    """
    This function converts a date string to a
    standard (canonical) format.
    Args:
        date_str: the date string to be converted
    Returns:
        the converted date string in the format "yyyy-mm-dd"
    """
    # date_str = date_str.strip(':')
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
                  'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
                  'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
                 }
    if '-' in date_str:
        yyyy = date_str.split('-')[0]
        mm = date_str.split('-')[1]
        dd = date_str.split('-')[2]
        return "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
    elif '/' in date_str:
        yyyy = date_str.split('/')[2]
        mm = date_str.split('/')[0]
        dd = date_str.split('/')[1]
        return "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))
    else:
        yyyy = date_str.split(' ')[2]
        mm = month_dict[date_str.split(' ')[0]]
        dd = date_str.split(' ')[1]
        return "{:d}-{:d}-{:d}".format(int(yyyy), int(mm), int(dd))

def handle_input(file_name):
    """
    This function takes in a file name, reads through the file, and 
    either inserts dates & events or reads events given a date.
    Args:
        file_name: the name of the file to be read
    Returns:
        None
    """
    file = open(file_name, 'r')
    date_collection = DateSet({})
    for line in file:
        canonical_date = ""
        # this splits on colon, to get the operation type and date, then
        # splits on white space to remove \n.  
        op_type_and_date = line.split(':')[0].strip().split()
        # Date is split on spaces if this condition is true
        if len(op_type_and_date) > 2:
            date = ' '.join(op_type_and_date[1:4])
            canonical_date = canonicalize_date(date)
        else:
            date = op_type_and_date[1]
            canonical_date = canonicalize_date(date)
        if line[0] == 'I':
            event_str = ':'.join(line.split(':')[1:]).strip()
            date_collection.add_date(canonical_date, event_str)
        elif line[0] == 'R':
            date_dict = date_collection.get_date_dict()
            # avoid key error by checking if key in dict
            if canonical_date in date_dict:
                for event in (
                    sorted(date_dict[canonical_date].get_event_list())
                ):
                    print(f"{canonical_date}: {event}")
        else:
            print("Error - Illegal operation.")

class Date:
    """
    This class represents a date and its associated events.
    """
    def __init__(self, canonical_date, event_list):
        """
        Initializes a Date object with the given canonical date and event list.
        Parameters:
            canonical_date (str): the canonical date of the event
            event_list (list): a list of events associated with the date
        """
        self._canonical_date = canonical_date
        self._event_list = event_list

    def add_event(self, event):
        """
        Adds the given event to the event list associated with the date.
        Parameters:
            event: the event to be added
        """
        self._event_list.append(event)
    
    def get_canonical_date(self):
        return self._canonical_date

    def get_event_list(self):
        return self._event_list
    
    def __str__(self):
        return f"Date({self._canonical_date}): {len(self._event_list)} events"

class DateSet:
    """
    This class represents a set of Date classes in a dictionary.
    """
    def __init__(self, date_dictionary):
        """
        this method initializes a dictionary to store Date objects
        and uses canonical dates as keys.
        """
        self._date_dictionary = date_dictionary

    def get_date_dict(self):
        return self._date_dictionary
    
    def add_date(self, date, event):
        """
        This method takes in a canonical date and event title and 
        adds them to the date dictionary. If the date is 
        not in the dictionary, it makes a new object.
        Parameters:
            date: the canonical date string
            event: the title of the event as a string
        """
        if date not in self._date_dictionary:
            self._date_dictionary[date] = Date(date, [])
            self._date_dictionary[date].add_event(event)
        else:
            self._date_dictionary[date].add_event(event)

    def __str__(self):
        cloned_dict = dict(self._date_dictionary)
        for key in self._date_dictionary:
            cloned_dict[key] = str(self._date_dictionary[key])
        return str(cloned_dict)
    
def main():
    file_name = input()
    # file_name = "in04.txt"
    handle_input(file_name)  

main()
