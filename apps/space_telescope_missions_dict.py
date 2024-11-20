# Create a dictionary of 5 space telescopes and their missions
space_telescope_missions = {
    'Hubble': 'Exploration of deep space',
    'Chandra': 'X-ray observations of black holes',
    'James Webb': 'Studying the early universe',
    'Spitzer': 'Infrared observations of galaxies',
    'Kepler': 'Searching for exoplanets'
}

# Print the entire dictionary
print("Space Telescope Missions Dictionary:", space_telescope_missions)

# Access and print the mission of the 3rd telescope
print("Mission of the third telescope (James Webb):", space_telescope_missions['James Webb'])

# Update the mission of the 1st telescope
space_telescope_missions['Hubble'] = 'Observing distant galaxies and supernovae'
print("Updated mission of the first telescope (Hubble):", space_telescope_missions['Hubble'])

# Delete the 4th telescope from the dictionary
del space_telescope_missions['Spitzer']
print("Dictionary after deleting the 4th telescope:", space_telescope_missions)

# Print the last key-value pair in the dictionary
last_key = list(space_telescope_missions.keys())[-1]
print("Last key-value pair:", last_key, ":", space_telescope_missions[last_key])
