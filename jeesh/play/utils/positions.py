def check_if_valid_position(position):
    if position[0] < 0 or position[0] > 10:
        return False
    if position[1] < 0 or position[1] > 10:
        return False
    if position[2] < 0 or position[2] > 10:
        return False
    return True