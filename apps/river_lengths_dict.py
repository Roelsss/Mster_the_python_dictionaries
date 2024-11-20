# Create a dictionary of 6 rivers and their lengths in kilometers
river_lengths = {
    'Amazon': 7050,
    'Nile': 6671,
    'Yangtze': 6300,
    'Mississippi': 3730,
    'Yenisei': 5539,
    'Ganges': 2525
}

# Print the entire dictionary
print("River Lengths Dictionary:", river_lengths)

# Access and print the length of the 2nd river
print("Length of the second river:", river_lengths['Nile'], "km")

# Update the length of the 5th river
river_lengths['Yenisei'] = 6000
print("Updated length of the fifth river:", river_lengths['Yenisei'], "km")

# Delete the 4th river from the dictionary
del river_lengths['Mississippi']
print("Dictionary after deleting the 4th river:", river_lengths)

# Print the last key-value pair in the dictionary
last_key = list(river_lengths.keys())[-1]
print("Last key-value pair:", last_key, ":", river_lengths[last_key], "km")
