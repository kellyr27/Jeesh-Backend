from play.utils.positions import check_if_valid_position

def get_current_army_poses(game_state, armyNum):
    soldier_poses = []
    for soldier in game_state[f'army{armyNum}']:
        if not soldier['dead']:
            soldier_poses.append(soldier['poses'][-1])

def get_current_army1_poses(game_state):
    return get_current_army_poses(game_state, 1)

def get_current_army2_poses(game_state):
    return get_current_army_poses(game_state, 2)

def get_current_army_current_positions(game_state, armyNum):
    soldier_positions = []
    for soldier in game_state[f'army{armyNum}']:
        if not soldier['dead']:
            soldier_positions.append(soldier['poses'][-1]['position'])

def get_current_army1_positions(game_state):
    return get_current_army_current_positions(game_state, 1)

def get_current_army2_positions(game_state):
    return get_current_army_current_positions(game_state, 2)


# Gets a list of all the legal moves for a given soldier
def get_soldier_legal_moves(solider_index, soldier_position, star_positions, soldier_positions):
    
    # Get the orientations available in the current position
    def get_legal_orientations(i, j, k):
        orientations = []

        if i == soldier_position[0] - 1:
            orientations.append('-x')
        elif i == soldier_position[0] + 1:
            orientations.append('+x')
        elif j == soldier_position[1] - 1:
            orientations.append('-y')
        elif j == soldier_position[1] + 1:
            orientations.append('+y')
        elif k == soldier_position[2] - 1:
            orientations.append('-z')
        elif k == soldier_position[2] + 1:
            orientations.append('+z')

        return orientations

    legal_moves = []

    for i in range(soldier_position[0] - 1, soldier_position[0] + 2):
        for j in range(soldier_position[1] - 1, soldier_position[1] + 2):
            for k in range(soldier_position[2] - 1, soldier_position[2] + 2):
                if [i, j, k] not in soldier_positions and [i, j, k] not in star_positions and check_if_valid_position([i, j, k]):
                    
                    # Get the orientations available in the current position and create a legal move for each orientation
                    orientations = get_legal_orientations(i, j, k)
                    for orientation in orientations:
                        legal_moves.append({
                            'soldierIndex': solider_index,
                            'position': [i, j, k],
                            'orientation': orientation
                        })

    return legal_moves

def get_army_legal_moves(game_state, armyNum):
    legal_moves = []
    army1_positions = get_current_army1_positions(game_state)
    army2_positions = get_current_army2_positions(game_state)
    star_positions = game_state['starsPositions']
    
    for index, soldier in enumerate(game_state[f'army{armyNum}']):
        if not soldier['dead']:
            soldier_legal_moves = get_soldier_legal_moves(index, soldier['poses'][-1]['position'], star_positions, army1_positions + army2_positions)
            legal_moves += soldier_legal_moves

    return legal_moves

def get_army1_legal_moves(game_state):
    return get_army_legal_moves(game_state, 1)

def get_army2_legal_moves(game_state):
    return get_army_legal_moves(game_state, 2)