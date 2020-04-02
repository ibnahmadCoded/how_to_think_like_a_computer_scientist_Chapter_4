def hours_in(number):
    """calculates number of hours from total number of seconds"""
    return number // 3600

def minutes_in(number):
    """calculates number of minutes from total number of seconds"""
    new_number = number - (hours_in(number) * 3600)
    return new_number // 60

def seconds_in(number):
    """calculates number of remaining seconds from total number of seconds
    after hours and minutes have been removed
    """
    new_number = number - ((minutes_in(number) * 60) + (hours_in(number) * 3600))
    return new_number
