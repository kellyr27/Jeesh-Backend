import json

# Step 1: Open the JSON file
with open('example_game.json', 'r') as file:
    # Step 2: Use json.load to load the JSON data into a Python object
    data = json.load(file)

# Now 'data' contains a Python dictionary representing the JSON content
print(data)