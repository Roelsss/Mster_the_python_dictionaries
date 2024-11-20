# Create a dictionary of 6 continents and a list of 3 countries for each
continent_countries = {
    'Africa': ['Nigeria', 'Egypt', 'South Africa'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['Germany', 'France', 'Italy'],
    'North America': ['USA', 'Canada', 'Mexico'],
    'South America': ['Brazil', 'Argentina', 'Chile'],
    'Australia': ['Australia', 'New Zealand', 'Fiji']
}

# Print the entire dictionary
print("Continent Countries Dictionary:", continent_countries)

# Access and print the countries of the 4th continent
print("Countries of the fourth continent:", continent_countries['North America'])

# Update the countries of the 5th continent
continent_countries['South America'] = ['Peru', 'Colombia', 'Ecuador']
print("Updated countries of the fifth continent:", continent_countries['South America'])

# Delete the 6th continent from the dictionary
del continent_countries['Australia']
print("Dictionary after deleting the 6th continent:", continent_countries)

# Print the last key-value pair in the dictionary
last_key = list(continent_countries.keys())[-1]
print("Last key-value pair:", last_key, ":", continent_countries[last_key])
