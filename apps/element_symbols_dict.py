
# Create a dictionary of 10 elements and their chemical symbols
element_symbols = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne'
}

# Print the entire dictionary
print("Element Symbols Dictionary:", element_symbols)

# Access and print the symbol of the 6th element
print("Symbol of the sixth element:", element_symbols['Carbon'])

# Update the symbol of the 8th element
element_symbols['Oxygen'] = 'O2'
print("Updated symbol of the eighth element:", element_symbols['Oxygen'])

# Delete the 9th element from the dictionary
del element_symbols['Fluorine']
print("Dictionary after deleting the 9th element:", element_symbols)

# Print the last key-value pair in the dictionary
last_key = list(element_symbols.keys())[-1]
print("Last key-value pair:", last_key, ":", element_symbols[last_key])
