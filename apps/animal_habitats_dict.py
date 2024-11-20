# Create a dictionary of 8 animals and their natural habitats
animal_habitats = {
    'Lion': 'Savannah',
    'Penguin': 'Antarctica',
    'Elephant': 'Grasslands',
    'Polar Bear': 'Arctic',
    'Kangaroo': 'Australian Outback',
    'Panda': 'Bamboo Forests',
    'Dolphin': 'Ocean',
    'Eagle': 'Mountains'
}

# Print the entire dictionary
print("Animal Habitats Dictionary:", animal_habitats)

# Access and print the habitat of the 3rd animal
print("Habitat of the third animal:", animal_habitats['Elephant'])

# Update the habitat of the 5th animal
animal_habitats['Kangaroo'] = 'Deserts'
print("Updated habitat of the fifth animal:", animal_habitats['Kangaroo'])

# Delete the 7th animal from the dictionary
del animal_habitats['Dolphin']
print("Dictionary after deleting the 7th animal:", animal_habitats)

# Print the last key-value pair in the dictionary
last_key = list(animal_habitats.keys())[-1]
print("Last key-value pair:", last_key, ":", animal_habitats[last_key])
