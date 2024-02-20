def sum_csv_string(csv_string):
    num_str_list = csv_string.split(',')
    nums_list = []
    for num in num_str_list:
        nums_list.append(float(num))
    return sum(nums_list)

print(sum_csv_string('11,22,-33'))