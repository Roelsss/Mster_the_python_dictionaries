# Create a dictionary of 10 software companies and their headquarters
software_companies = {
    'Microsoft': 'Redmond, USA',
    'Google': 'Mountain View, USA',
    'Apple': 'Cupertino, USA',
    'Amazon': 'Seattle, USA',
    'Facebook': 'Menlo Park, USA',
    'IBM': 'Armonk, USA',
    'Oracle': 'Redwood City, USA',
    'Adobe': 'San Jose, USA',
    'SAP': 'Walldorf, Germany',
    'Salesforce': 'San Francisco, USA'
}

# Print the entire dictionary
print("Software Companies Dictionary:", software_companies)

# Access and print the headquarters of the 3rd company
print("Headquarters of the third company:", software_companies['Apple'])

# Update the headquarters of the 8th company
software_companies['Adobe'] = 'San Francisco, USA'
print("Updated headquarters of the eighth company:", software_companies['Adobe'])

# Delete the 9th company from the dictionary
del software_companies['SAP']
print("Dictionary after deleting the 9th company:", software_companies)

# Print the last key-value pair in the dictionary
last_key = list(software_companies.keys())[-1]
print("Last key-value pair:", last_key, ":", software_companies[last_key])
