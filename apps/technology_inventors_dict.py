# Create a dictionary of 6 technologies and their inventors
technology_inventors = {
    'Telephone': 'Alexander Graham Bell',
    'Lightbulb': 'Thomas Edison',
    'Airplane': 'Wright Brothers',
    'Computer': 'Charles Babbage',
    'Penicillin': 'Alexander Fleming',
    'Internet': 'Vinton Cerf & Robert Kahn'
}

# Print the entire dictionary
print("Technology Inventors Dictionary:", technology_inventors)

# Access and print the inventor of the 4th technology
print("Inventor of the fourth technology:", technology_inventors['Computer'])

# Update the inventor of the 2nd technology
technology_inventors['Lightbulb'] = 'Joseph Swan'
print("Updated inventor of the second technology:", technology_inventors['Lightbulb'])

# Delete the 6th technology from the dictionary
del technology_inventors['Internet']
print("Dictionary after deleting the 6th technology:", technology_inventors)

# Print the last key-value pair in the dictionary
last_key = list(technology_inventors.keys())[-1]
print("Last key-value pair:", last_key, ":", technology_inventors[last_key])
