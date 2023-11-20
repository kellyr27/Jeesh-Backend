'''
Example of a game JSON
{
    "starsPositions": [
        [5,5,5],
        [5,5,6],
    ],
    "currentIndex": 3,
    "army1": [
        {
            "id": 1,
            "dead": false,
            "positions": [
                {
                    position: [1, 1, 1],
                    orientation: "+x"
                },
                {
                    position: [1, 1, 1],
                    orientation: "+x"
                }
            ]
        },
        {
            "id": 2,
            "dead": false,
            "positions": [
                {
                    position: [1, 1, 2],
                    orientation: "+x"
                },
                {
                    position: [1, 1, 3],
                    orientation: "+x"
                }
            ]
        },
    ],
    "army2": [
        {
            "id": 1,
            "dead": false,
            "positions": [
                {
                    position: [1, 1, 1],
                    orientation: "+x"
                },
                {
                    position: [1, 1, 1],
                    orientation: "+x"
                }
            ]
        }
    ]
}
'''


def initialize_game():
    pass

def get_legal_moves():
    pass

def apply_move():
    pass

def is_terminal():
    pass

def get_best_move():
    pass