from play.core.stars import generate_star_coordinates
from play.core.game_parameters import STARTING_POSES, DOOR_POSITIONS
from play.core.moves import get_army1_legal_moves, get_army2_legal_moves, get_current_army2_positions, get_current_army1_positions, get_current_army1_poses, get_current_army2_poses
from play.core.attacking_zone import get_soldier_attacking_zone, get_army1_attacking_zone, get_army2_attacking_zone

# Initialize the game
def initialize_game():
    return {
        'starsPositions': generate_star_coordinates(),
        'currentMoveIndex': 1,
        'army1': STARTING_POSES['army1'],
        'army2': STARTING_POSES['army2']
    }

# Gets a list of all the legal moves for the Army to move
def get_legal_moves(game_state):
    if game_state['currentMoveIndex'] % 2 == 1:
        return get_army1_legal_moves(game_state)
    else:
        return get_army2_legal_moves(game_state)

def apply_move(move, game_state):
    # Check if the move was legal
    legal_moves = get_legal_moves(game_state)
    if move not in legal_moves:
        raise Exception('Invalid move')
    
    # Apply the move
    army1_positions = get_current_army1_positions(game_state)
    army2_positions = get_current_army2_positions(game_state)

    # First check if the Soldier that moved has killed any opposing Soliders
    active_soldier_attacking_zone = get_soldier_attacking_zone(move['position'], move['orientation'])
    
    if game_state['currentMoveIndex'] % 2 == 1:
        for soldier in game_state['army2']:
            if not soldier['dead']:
                soldier_current_position = set(soldier['poses'][-1]['position'])
                if soldier_current_position in active_soldier_attacking_zone:
                    soldier['dead'] = True
    else:
        for soldier in game_state['army1']:
            if not soldier['dead']:
                soldier_current_position = set(soldier['poses'][-1]['position'])
                if soldier_current_position in active_soldier_attacking_zone:
                    soldier['dead'] = True
    
    # Second check if the Solider that moved has entered the opposing Armies attacking zone
    if game_state['currentMoveIndex'] % 2 == 1:
        army2_attacking_zone = get_army2_attacking_zone(game_state)

        if set(move['position']) in army2_attacking_zone:
            game_state['army1'][move['soldierIndex']]['dead'] = True
    else:
        army1_attacking_zone = get_army1_attacking_zone(game_state)

        if set(move['position']) in army1_attacking_zone:
            game_state['army2'][move['soldierIndex']]['dead'] = True

    # Check Draw conditions
    is_army1_dead = check_if_army_is_dead(game_state['army1'])
    is_army2_dead = check_if_army_is_dead(game_state['army2'])
    has_army1_entered_door = check_if_army1_entered_door(game_state['army1'])
    has_army2_entered_door = check_if_army2_entered_door(game_state['army2'])

    if is_army1_dead and not is_army2_dead:
        game_state['isGameOver'] = True
        game_state['gameResult'] = 'Army 2 Wins by Default'
    elif is_army2_dead and not is_army1_dead:
        game_state['isGameOver'] = True
        game_state['gameResult'] = 'Army 1 Wins by Default'
    elif is_army1_dead and is_army2_dead:
        game_state['isGameOver'] = True
        game_state['gameResult'] = 'Draw by Default'
    elif has_army1_entered_door and not has_army2_entered_door:
        game_state['isGameOver'] = True
        game_state['gameResult'] = 'Army 1 Wins by Entering the Door'
    elif has_army2_entered_door and not has_army1_entered_door:
        game_state['isGameOver'] = True
        game_state['gameResult'] = 'Army 2 Wins by Entering the Door'
    else:
        return False

    # Check Win conditions

    # Update the game state if game is still in progress


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