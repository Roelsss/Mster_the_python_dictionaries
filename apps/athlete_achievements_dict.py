# Create a dictionary of 8 athletes and their greatest achievements
athlete_achievements = {
    'Usain Bolt': '8 Olympic Gold Medals',
    'Michael Phelps': '23 Olympic Gold Medals',
    'Serena Williams': '23 Grand Slam Singles Titles',
    'Cristiano Ronaldo': '5 Ballon d\'Or Awards',
    'LeBron James': '4 NBA Championships',
    'Tom Brady': '7 Super Bowl Titles',
    'Tiger Woods': '15 Major Championships',
    'Simone Biles': '7 Olympic Medals'
}

# Print the entire dictionary
print("Athlete Achievements Dictionary:", athlete_achievements)

# Access and print the achievement of the 5th athlete
print("Achievement of the fifth athlete (LeBron James):", athlete_achievements['LeBron James'])

# Update the achievement of the 3rd athlete
athlete_achievements['Serena Williams'] = '24 Grand Slam Singles Titles'
print("Updated achievement of the third athlete (Serena Williams):", athlete_achievements['Serena Williams'])

# Delete the 7th athlete from the dictionary
del athlete_achievements['Tiger Woods']
print("Dictionary after deleting the 7th athlete:", athlete_achievements)

# Print the last key-value pair in the dictionary
last_key = list(athlete_achievements.keys())[-1]
print("Last key-value pair:", last_key, ":", athlete_achievements[last_key])
