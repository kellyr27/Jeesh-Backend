import random

# Generate a set of star coordinates
def generate_star_coordinates():
    # Determine a random number of stars to generate
    num_stars = random.randint(0, 81)

    # Create a list of star coordinates
    star_coordinates = []
    for i in range(num_stars):
        star_coordinates.add(
            [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
        )
    
    return star_coordinates