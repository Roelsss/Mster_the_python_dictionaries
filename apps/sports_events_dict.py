# Create a dictionary of 7 sports events and their corresponding years
sports_events = {
    'World Cup 2018': 2018,
    'Olympics 2020': 2020,
    'Super Bowl LV': 2021,
    'UEFA Champions League Final': 2021,
    'NBA Finals 2021': 2021,
    'Wimbledon 2021': 2021,
    'FIFA World Cup 2022': 2022
}

# Print the entire dictionary
print("Sports events and their years:", sports_events)

# Access and print the year of the 3rd sports event
print("Year of the 3rd sports event (Super Bowl LV):", sports_events['Super Bowl LV'])

# Update the year of the 6th sports event
sports_events['Wimbledon 2021'] = 2022
print("Updated year of the 6th sports event (Wimbledon 2021):", sports_events['Wimbledon 2021'])

# Delete the 5th sports event from the dictionary
del sports_events['NBA Finals 2021']
print("Dictionary after deleting the 5th sports event (NBA Finals 2021):", sports_events)

# Print the last key-value pair in the dictionary
last_key = list(sports_events.keys())[-1]
print("Last key-value pair:", last_key, ":", sports_events[last_key])
