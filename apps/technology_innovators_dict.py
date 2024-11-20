# Create a dictionary of 8 technologies and their innovators
technology_innovators = {
    'Light Bulb': 'Thomas Edison',
    'Telephone': 'Alexander Graham Bell',
    'Computer': 'Charles Babbage',
    'Internet': 'Vint Cerf',
    'Electricity': 'Nikola Tesla',
    'Penicillin': 'Alexander Fleming',
    'Automobile': 'Karl Benz',
    'Airplane': 'Wright Brothers'
}

# Print the entire dictionary
print("Technologies and their innovators:", technology_innovators)

# Access and print the innovator of the 4th technology
print("Innovator of the 4th technology (Internet):", technology_innovators['Internet'])

# Update the innovator of the 2nd technology
technology_innovators['Telephone'] = 'Antonio Meucci'
print("Updated innovator of the 2nd technology (Telephone):", technology_innovators['Telephone'])

# Delete the 6th technology from the dictionary
del technology_innovators['Penicillin']
print("Dictionary after deleting the 6th technology (Penicillin):", technology_innovators)

# Print the last key-value pair in the dictionary
last_key = list(technology_innovators.keys())[-1]
print("Last key-value pair:", last_key, ":", technology_innovators[last_key])
