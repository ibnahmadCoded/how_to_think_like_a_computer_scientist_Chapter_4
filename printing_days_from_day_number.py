def day_name(number):
    """converts an integer to day, assuming sunday is 0."""
    days = ["Sunday", "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday"]
    if number <= 6:
        return days[number]

