def date_to_word(date):
    # assume date is properly formatted mm/dd/yyyy
    # parse string for month
    month = date[:date.find("/"):]
    # parse remaining string for day
    date = date[date.find("/") + 1::]
    day = date[:date.find("/"):]

    # store month conversion as dict
    month_dict = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    month_word = month_dict.get(month)

    #day edge cases: 1st, 2nd, 3rd, 21st, 22nd, 23rd, 31st
    if int(day) in [1, 2, 3, 21, 22, 23, 31]:
        if int(day)%10 == 1:
            day_suffix = "st"
        elif int(day)%10 == 2:
            day_suffix = "nd"
        elif int(day) % 10 == 3:
            day_suffix = "rd"
    else:
        day_suffix = "th"

    result = "%s %s%s" %(month_word, day, day_suffix)
    return print(result)


