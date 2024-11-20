# Create a dictionary of 10 sports and their most famous players
sports_players = {
    'Soccer': 'Lionel Messi',
    'Basketball': 'Michael Jordan',
    'Tennis': 'Serena Williams',
    'Cricket': 'Virat Kohli',
    'Swimming': 'Michael Phelps',
    'Boxing': 'Muhammad Ali',
    'Golf': 'Tiger Woods',
    'Formula 1': 'Lewis Hamilton',
    'Baseball': 'Babe Ruth',
    'Hockey': 'Wayne Gretzky'
}

# Print the entire dictionary
print("Sports Players Dictionary:", sports_players)

# Access and print the player of the 4th sport
print("Player of the fourth sport:", sports_players['Cricket'])

# Update the player of the 6th sport
sports_players['Boxing'] = 'Mike Tyson'
print("Updated player of the sixth sport:", sports_players['Boxing'])

# Delete the 10th sport from the dictionary
del sports_players['Hockey']
print("Dictionary after deleting the 10th sport:", sports_players)

# Print the last key-value pair in the dictionary
last_key = list(sports_players.keys())[-1]
print("Last key-value pair:", last_key, ":", sports_players[last_key])
