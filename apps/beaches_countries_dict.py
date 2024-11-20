# Create a dictionary of 8 beaches and the countries they are located in
beaches_countries = {
    'Bondi Beach': 'Australia',
    'Waikiki Beach': 'USA',
    'Copacabana Beach': 'Brazil',
    'Maya Bay': 'Thailand',
    'Playa del Carmen': 'Mexico',
    'Whitehaven Beach': 'Australia',
    'Maldives Beach': 'Maldives',
    'Anse Source d\'Argent': 'Seychelles'
}

# Print the entire dictionary
print("Beaches and their countries:", beaches_countries)

# Access and print the country of the 3rd beach
print("Country of the 3rd beach (Copacabana Beach):", beaches_countries['Copacabana Beach'])

# Update the country of the 6th beach
beaches_countries['Whitehaven Beach'] = 'Australia (Updated Location)'
print("Updated country of the 6th beach (Whitehaven Beach):", beaches_countries['Whitehaven Beach'])

# Delete the 5th beach from the dictionary
del beaches_countries['Playa del Carmen']
print("Dictionary after deleting the 5th beach (Playa del Carmen):", beaches_countries)

# Print the last key-value pair in the dictionary
last_key = list(beaches_countries.keys())[-1]
print("Last key-value pair:", last_key, ":", beaches_countries[last_key])
