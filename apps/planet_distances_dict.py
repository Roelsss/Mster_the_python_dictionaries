# Create a dictionary of 8 planets and their distances from the sun (in million kilometers)
planet_distances = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.3,
    'Saturn': 1427,
    'Uranus': 2871,
    'Neptune': 4497.1
}

# Print the entire dictionary
print("Planet Distances from the Sun:", planet_distances)

# Access and print the distance of the 3rd planet
print("Distance of the third planet (Earth):", planet_distances['Earth'])

# Update the distance of the 5th planet
planet_distances['Jupiter'] = 800.0
print("Updated distance of the fifth planet (Jupiter):", planet_distances['Jupiter'])

# Delete the 7th planet from the dictionary
del planet_distances['Uranus']
print("Dictionary after deleting the 7th planet:", planet_distances)

# Print the last key-value pair in the dictionary
last_key = list(planet_distances.keys())[-1]
print("Last key-value pair:", last_key, ":", planet_distances[last_key])
