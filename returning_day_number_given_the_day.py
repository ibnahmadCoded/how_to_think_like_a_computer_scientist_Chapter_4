def day_num(day):
    """returns day number if day name is given."""
    days = [(1, "Sunday"), (2, "Monday"), (3, "Tuesday"), (4, "Wednessday"),
            (5, "Thursday"), (6, "Friday"), (7, "Saturday")]
    for n, d in days:
        if d == day:
            return n
