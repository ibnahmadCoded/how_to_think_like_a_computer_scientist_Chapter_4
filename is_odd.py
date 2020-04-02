def is_even(n):
    """checks if a number, n is even"""
    return n % 2 == 0

def is_odd(n):
    """checks if a number, n is odd"""
    if is_even(n):
        return False
    return True
