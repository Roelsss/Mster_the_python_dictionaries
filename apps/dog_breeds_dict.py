# Create a dictionary of 10 dog breeds and their sizes
dog_breeds = {
    'Labrador Retriever': 'Large',
    'Beagle': 'Medium',
    'Bulldog': 'Medium',
    'German Shepherd': 'Large',
    'Poodle': 'Medium',
    'Chihuahua': 'Small',
    'Golden Retriever': 'Large',
    'Rottweiler': 'Large',
    'Yorkshire Terrier': 'Small',
    'Boxer': 'Medium'
}

# Print the entire dictionary
print("Dog Breeds Dictionary:", dog_breeds)

# Access and print the size of the 5th breed
print("Size of the fifth breed (Poodle):", dog_breeds['Poodle'])

# Update the size of the 8th breed
dog_breeds['Rottweiler'] = 'Medium'
print("Updated size of the eighth breed (Rottweiler):", dog_breeds['Rottweiler'])

# Delete the 6th breed from the dictionary
del dog_breeds['Chihuahua']
print("Dictionary after deleting the 6th breed:", dog_breeds)

# Print the last key-value pair in the dictionary
last_key = list(dog_breeds.keys())[-1]
print("Last key-value pair:", last_key, ":", dog_breeds[last_key])
