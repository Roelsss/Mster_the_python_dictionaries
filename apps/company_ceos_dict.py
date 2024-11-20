# Create a dictionary of 10 companies and their current CEOs
company_ceos = {
    'Apple': 'Tim Cook',
    'Microsoft': 'Satya Nadella',
    'Amazon': 'Andy Jassy',
    'Tesla': 'Elon Musk',
    'Google': 'Sundar Pichai',
    'Meta': 'Mark Zuckerberg',
    'IBM': 'Arvind Krishna',
    'Netflix': 'Ted Sarandos',
    'Oracle': 'Safra Catz',
    'Salesforce': 'Marc Benioff'
}

# Print the entire dictionary
print("Company CEOs Dictionary:", company_ceos)

# Access and print the CEO of the 6th company
print("CEO of the sixth company:", company_ceos['Meta'])

# Update the CEO of the 3rd company
company_ceos['Amazon'] = 'Jeff Bezos'
print("Updated CEO of the third company:", company_ceos['Amazon'])

# Delete the 9th company from the dictionary
del company_ceos['Oracle']
print("Dictionary after deleting the 9th company:", company_ceos)

# Print the last key-value pair in the dictionary
last_key = list(company_ceos.keys())[-1]
print("Last key-value pair:", last_key, ":", company_ceos[last_key])
