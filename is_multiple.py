def is_multiple(m, n):
    """Checks if n is a multiple of m"""
    if is_factor(n, m):
        return True
    return False

def is_factor(f, n):
    """checks if f is a factor of n"""
    return (n % f) == 0
