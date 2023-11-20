'''
Example of a game JSON
{
    "starsPositions": [
        [5,5,5],
        [5,5,6],
    ],
    "currentMoveIndex": 3,
    "army1": [
        {
            "dead": false,
            "poses": [
                {
                    moveIndex: 0,
                    position: [1, 1, 1],
                    orientation: "+x"
                }
            ]
        },
        {
            "dead": false,
            "poses": [
                {
                    moveIndex: 0,
                    position: [1, 1, 2],
                    orientation: "+x"
                },
                {
                    moveIndex: 1,
                    position: [1, 1, 3],
                    orientation: "+x"
                }
            ]
        },
    ],
    "army2": [
        {
            "dead": false,
            "poses": [
                {
                    moveIndex: 0,
                    position: [1, 1, 1],
                    orientation: "+x"
                },
                {
                    moveIndex: 2,
                    position: [1, 1, 1],
                    orientation: "+x"
                }
            ]
        }
    ]
}
'''
from play.core.stars import generate_star_coordinates

class Soldier:
    def __init__(self, id, dead, positions) -> None:
        self.id = id
        self.dead = dead
        self.positions = positions

class Game:
    
    def __init__(self, game_json) -> None:
        self.star_positions = star_positions




# def extract_current_soldier_positions(game_json):
#     pass


# def initialize_game():
#     # Get random star positions
#     star_positions = generate_star_coordinates()



# def get_legal_moves():
#     pass

# def apply_move():
#     pass

# def is_terminal():
#     pass

# def get_best_move():
#     pass