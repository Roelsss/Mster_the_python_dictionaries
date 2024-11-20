# Create a dictionary of 8 animals and their sounds
animal_sounds = {
    'Dog': 'Bark',
    'Cat': 'Meow',
    'Cow': 'Moo',
    'Sheep': 'Baa',
    'Duck': 'Quack',
    'Horse': 'Neigh',
    'Frog': 'Ribbit',
    'Lion': 'Roar'
}

# Print the entire dictionary
print("Animal Sounds Dictionary:", animal_sounds)

# Access and print the sound of the 4th animal
print("Sound of the fourth animal:", animal_sounds['Sheep'])

# Update the sound of the 7th animal
animal_sounds['Frog'] = 'Croak'
print("Updated sound of the seventh animal:", animal_sounds['Frog'])

# Delete the entry of the 5th animal
del animal_sounds['Duck']
print("Dictionary after deleting 5th animal:", animal_sounds)

# Print the last key-value pair in the dictionary
last_key = list(animal_sounds.keys())[-1]
print("Last key-value pair:", last_key, ":", animal_sounds[last_key])
