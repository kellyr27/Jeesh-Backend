from play.utils.positions import check_if_valid_position

# Given a Soldiers position, return the attacking zone of that Soldier
# Attacking zone is a list of all the Cubes that the Soldier can attack
def get_soldier_attacking_zone(soldier_position, soldier_orientation):
    attacking_zone = set()

    if soldier_orientation == '+x':
        for i in range(soldier_position[0] + 1, soldier_position[0] + 4):
            for j in range(soldier_position[1] - 1, soldier_position[1] + 2):
                for k in range(soldier_position[2] - 1, soldier_position[2] + 2):
                    if check_if_valid_position((i, j, k)):
                        attacking_zone.add((i, j, k))
    elif soldier_orientation == '-x':
        for i in range(soldier_position[0] - 3, soldier_position[0]):
            for j in range(soldier_position[1] - 1, soldier_position[1] + 2):
                for k in range(soldier_position[2] - 1, soldier_position[2] + 2):
                    if check_if_valid_position((i, j, k)):
                        attacking_zone.add((i, j, k))
    elif soldier_orientation == '+y':
        for i in range(soldier_position[0] - 1, soldier_position[0] + 2):
            for j in range(soldier_position[1] + 1, soldier_position[1] + 4):
                for k in range(soldier_position[2] - 1, soldier_position[2] + 2):
                    if check_if_valid_position((i, j, k)):
                        attacking_zone.add((i, j, k))
    elif soldier_orientation == '-y':
        for i in range(soldier_position[0] - 1, soldier_position[0] + 2):
            for j in range(soldier_position[1] - 3, soldier_position[1]):
                for k in range(soldier_position[2] - 1, soldier_position[2] + 2):
                    if check_if_valid_position((i, j, k)):
                        attacking_zone.add((i, j, k))
    elif soldier_orientation == '+z':
        for i in range(soldier_position[0] - 1, soldier_position[0] + 2):
            for j in range(soldier_position[1] - 1, soldier_position[1] + 2):
                for k in range(soldier_position[2] + 1, soldier_position[2] + 4):
                    if check_if_valid_position((i, j, k)):
                        attacking_zone.add((i, j, k))
    elif soldier_orientation == '-z':
        for i in range(soldier_position[0] - 1, soldier_position[0] + 2):
            for j in range(soldier_position[1] - 1, soldier_position[1] + 2):
                for k in range(soldier_position[2] - 3, soldier_position[2]):
                    if check_if_valid_position((i, j, k)):
                        attacking_zone.add((i, j, k))

    return attacking_zone

# Given a list of Soldiers (Army), return a list of all the Cubes that the Soldiers can attack
def get_armies_attacking_zone(soldiers_current_poses):
    attacking_zone = set()

    for soldier_pose in soldiers_current_poses:
        attacking_zone.update(get_soldier_attacking_zone(soldier_pose.position, soldier_pose.orientation))

    return attacking_zone

# Given a Soldiers position, return if the Soldier is in an armies attacking zone
def is_soldier_in_attacking_zone(soldier_position, attacking_zone):
    return soldier_position in attacking_zone

