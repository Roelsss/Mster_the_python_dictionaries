# Create a dictionary of 10 cities and their populations
city_population = {
    'New York': 8419600,
    'Los Angeles': 3980400,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'Philadelphia': 1584200,
    'San Antonio': 1547200,
    'San Diego': 1423851,
    'Dallas': 1343573,
    'San Jose': 1035317
}

# Print the entire dictionary
print("City Population Dictionary:", city_population)

# Access and print the population of the 6th city
print("Population of the sixth city:", city_population['Philadelphia'])

# Update the population of the 3rd city
city_population['Chicago'] = 2750000
print("Updated population of the third city:", city_population['Chicago'])

# Delete the 9th city from the dictionary
del city_population['Dallas']
print("Dictionary after deleting the 9th city:", city_population)

# Print the last key-value pair in the dictionary
last_key = list(city_population.keys())[-1]
print("Last key-value pair:", last_key, ":", city_population[last_key])
