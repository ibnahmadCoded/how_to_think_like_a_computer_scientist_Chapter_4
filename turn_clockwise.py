def turn_clockwise(direction):
    """Returns the next clockwise direction when supplied with current one."""
    directions = ["N", "E", "S", "W"]
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
