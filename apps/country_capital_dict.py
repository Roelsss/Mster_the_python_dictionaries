# Create a dictionary of 12 countries and their capitals
country_capital = {
    'USA': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'UK': 'London',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Japan': 'Tokyo',
    'India': 'New Delhi',
    'Australia': 'Canberra',
    'Brazil': 'Brasilia',
    'Russia': 'Moscow',
    'South Africa': 'Pretoria'
}

# Print the entire dictionary
print("Country-Capital Dictionary:", country_capital)

# Access and print the capital of the 5th country
print("Capital of the fifth country:", country_capital['Germany'])

# Update the capital of the 8th country
country_capital['India'] = 'Delhi'
print("Updated capital of the eighth country:", country_capital['India'])

# Delete the 11th country from the dictionary
del country_capital['Russia']
print("Dictionary after deleting the 11th country:", country_capital)

# Print the last key-value pair in the dictionary
last_key = list(country_capital.keys())[-1]
print("Last key-value pair:", last_key, ":", country_capital[last_key])
