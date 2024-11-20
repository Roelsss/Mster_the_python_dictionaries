# Create a dictionary of 8 historical events and their years
historical_events = {
    'Moon Landing': 1969,
    'Fall of the Berlin Wall': 1989,
    'World War II Ended': 1945,
    'Declaration of Independence': 1776,
    'Civil Rights Act Signed': 1964,
    'Titanic Sinks': 1912,
    'First Man on the Moon': 1969,
    'Renaissance Begins': 14th Century
}

# Print the entire dictionary
print("Historical Events Dictionary:", historical_events)

# Access and print the year of the 2nd event
print("Year of the second event (Fall of the Berlin Wall):", historical_events['Fall of the Berlin Wall'])

# Update the year of the 7th event
historical_events['First Man on the Moon'] = 1968
print("Updated year of the seventh event (First Man on the Moon):", historical_events['First Man on the Moon'])

# Delete the 5th event from the dictionary
del historical_events['Civil Rights Act Signed']
print("Dictionary after deleting the 5th event:", historical_events)

# Print the last key-value pair in the dictionary
last_key = list(historical_events.keys())[-1]
print("Last key-value pair:", last_key, ":", historical_events[last_key])
