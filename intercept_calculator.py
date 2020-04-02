def slope(x1, y1, x2, y2):
    """calculates slope of a line given the coordinates"""
    return ((y2 - y1) / (x2 - x1))

def intercept(x1, y1, x2, y2):
    """claculates intercept through d slope"""
    s = slope(x1, y1, x2, y2) #calculate the slope
    intercept = y1 - (s * x1)
    return intercept
