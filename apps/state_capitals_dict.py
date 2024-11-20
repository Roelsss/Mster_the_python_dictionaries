# Create a dictionary of 10 states and their capitals
state_capitals = {
    'California': 'Sacramento',
    'Texas': 'Austin',
    'Florida': 'Tallahassee',
    'New York': 'Albany',
    'Illinois': 'Springfield',
    'Ohio': 'Columbus',
    'Georgia': 'Atlanta',
    'North Carolina': 'Raleigh',
    'Michigan': 'Lansing',
    'Pennsylvania': 'Harrisburg'
}

# Print the entire dictionary
print("State Capitals Dictionary:", state_capitals)

# Access and print the capital of the 4th state
print("Capital of the fourth state (New York):", state_capitals['New York'])

# Update the capital of the 9th state
state_capitals['Michigan'] = 'Detroit'
print("Updated capital of the ninth state (Michigan):", state_capitals['Michigan'])

# Delete the 7th state from the dictionary
del state_capitals['Georgia']
print("Dictionary after deleting the 7th state:", state_capitals)

# Print the last key-value pair in the dictionary
last_key = list(state_capitals.keys())[-1]
print("Last key-value pair:", last_key, ":", state_capitals[last_key])
