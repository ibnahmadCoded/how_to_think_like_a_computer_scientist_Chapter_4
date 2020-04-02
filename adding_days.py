def day_add(day, amount):
    """returns day after adding a number of days"""
    days = [(1, "Sunday"), (2, "Monday"), (3, "Tuesday"), (4, "Wednessday"), (5, "Thursday"),
            (6, "Friday"), (7, "Saturday")]

    #find the number that corresponds to the day in the days list
    for n, d in days:
        if d == day:
            day_number = n
            break

    #calculate the new day using the modulus    
    new_day_num = (amount % 7) + day_number

    #result of modulus calculation above might be greater than needed
    if new_day_num > 7:
        new_day_num = new_day_num % 7

    #find the day corresponding to the number
    for n, d in days:
        if n == new_day_num:
            new_day = d
            break

    return new_day 
    
