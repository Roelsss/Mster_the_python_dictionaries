# Create a dictionary of 8 space missions and their launching countries
space_missions = {
    'Apollo 11': 'USA',
    'Sputnik 1': 'Soviet Union',
    'Chandrayaan-3': 'India',
    'Mars Rover Perseverance': 'USA',
    'Tiangong': 'China',
    'Hubble Space Telescope': 'USA',
    'Rosetta': 'European Space Agency',
    'Artemis I': 'USA'
}

# Print the entire dictionary
print("Space Missions Dictionary:", space_missions)

# Access and print the launching country of the 3rd mission
print("Launching country of the third mission:", space_missions['Chandrayaan-3'])

# Update the launching country of the 5th mission
space_missions['Tiangong'] = 'People\'s Republic of China'
print("Updated launching country of the fifth mission:", space_missions['Tiangong'])

# Delete the 8th mission from the dictionary
del space_missions['Artemis I']
print("Dictionary after deleting the 8th mission:", space_missions)

# Print the last key-value pair in the dictionary
last_key = list(space_missions.keys())[-1]
print("Last key-value pair:", last_key, ":", space_missions[last_key])
