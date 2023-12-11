from play.core.stars import generate_star_coordinates
from play.core.game_parameters import STARTING_POSES, DOOR_POSITIONS

# Initialize the game
def initialize_game():
    return {
        'starsPositions': generate_star_coordinates(),
        'currentMoveIndex': 1,
        'army1': STARTING_POSES['army1'],
        'army2': STARTING_POSES['army2']
    }

def get_legal_moves(game_state):
    pass


# def apply_move():
#     pass

def check_if_army_is_dead(army):
    for soldier in army:
        if not soldier['dead']:
            return False
    return True

# Check if Army 1 has entered the Army 2 door
def check_if_army1_entered_door(army1):
    for soldier in army1:
        # Check if soldier is not dead last position
        if not soldier['dead'] and soldier['position'][-1] == DOOR_POSITIONS['army2']:
            return True

    return False

# Check if Army 2 has entered the Army 1 door
def check_if_army2_entered_door(army2):
    for soldier in army2:
        # Check if soldier is not dead last position
        if not soldier['dead'] and soldier['position'][-1] == DOOR_POSITIONS['army1']:
            return True

    return False


def is_terminal(game_state):
    is_army1_dead = check_if_army_is_dead(game_state['army1'])
    is_army2_dead = check_if_army_is_dead(game_state['army2'])

    if is_army1_dead or is_army2_dead:
        return True
    
    if check_if_army1_entered_door(game_state['army1']):
        return True

    return False

# def get_best_move():
#     pass