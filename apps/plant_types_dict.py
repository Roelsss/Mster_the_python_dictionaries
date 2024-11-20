# Create a dictionary of 8 plants and their types
plant_types = {
    'Rose': 'Shrub',
    'Oak': 'Tree',
    'Basil': 'Herb',
    'Tulip': 'Flower',
    'Cactus': 'Succulent',
    'Sunflower': 'Flower',
    'Lavender': 'Herb',
    'Pine': 'Tree'
}

# Print the entire dictionary
print("Plant Types Dictionary:", plant_types)

# Access and print the type of the 5th plant
print("Type of the fifth plant (Cactus):", plant_types['Cactus'])

# Update the type of the 2nd plant
plant_types['Oak'] = 'Deciduous Tree'
print("Updated type of the second plant (Oak):", plant_types['Oak'])

# Delete the 6th plant from the dictionary
del plant_types['Sunflower']
print("Dictionary after deleting the 6th plant:", plant_types)

# Print the last key-value pair in the dictionary
last_key = list(plant_types.keys())[-1]
print("Last key-value pair:", last_key, ":", plant_types[last_key])
