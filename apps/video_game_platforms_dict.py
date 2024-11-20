# Create a dictionary of 8 video games and their platforms
video_game_platforms = {
    'The Last of Us': 'PlayStation',
    'Halo': 'Xbox',
    'Minecraft': 'Multi-platform',
    'Super Mario Bros': 'Nintendo',
    'Fortnite': 'Multi-platform',
    'The Witcher 3': 'PC',
    'Grand Theft Auto V': 'Multi-platform',
    'Zelda: Breath of the Wild': 'Nintendo'
}

# Print the entire dictionary
print("Video Game Platforms Dictionary:", video_game_platforms)

# Access and print the platform of the 2nd video game
print("Platform of the second video game:", video_game_platforms['Halo'])

# Update the platform of the 6th video game
video_game_platforms['The Witcher 3'] = 'PC, PlayStation, Xbox'
print("Updated platform of the sixth video game:", video_game_platforms['The Witcher 3'])

# Delete the 4th video game from the dictionary
del video_game_platforms['Super Mario Bros']
print("Dictionary after deleting the 4th video game:", video_game_platforms)

# Print the last key-value pair in the dictionary
last_key = list(video_game_platforms.keys())[-1]
print("Last key-value pair:", last_key, ":", video_game_platforms[last_key])
