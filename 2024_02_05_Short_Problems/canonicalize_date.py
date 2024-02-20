def canonicalize_date(date_str):
    month_dict = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    if '-' in date_str:
        yyyy = date_str.split('-')[0]
        mm = date_str.split('-')[1]
        dd = date_str.split('-')[2]
        return "{:d}-{:d}-{:d}".format( int(yyyy), int(mm), int(dd))
    elif '/' in date_str:
        yyyy = date_str.split('/')[2]
        mm = date_str.split('/')[0]
        dd = date_str.split('/')[1]
        return "{:d}-{:d}-{:d}".format( int(yyyy), int(mm), int(dd))
    else:
        yyyy = date_str.split(' ')[2]
        mm = month_dict[date_str.split(' ')[0]]
        dd = date_str.split(' ')[1]
        return "{:d}-{:d}-{:d}".format( int(yyyy), int(mm), int(dd))
