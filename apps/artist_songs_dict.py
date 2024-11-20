# Create a dictionary of 8 artists and their top songs
artist_songs = {
    'Ariana Grande': 'Thank U, Next',
    'Drake': 'Hotline Bling',
    'Ed Sheeran': 'Shape of You',
    'Billie Eilish': 'Bad Guy',
    'Taylor Swift': 'Shake It Off',
    'Beyoncé': 'Single Ladies',
    'Kendrick Lamar': 'HUMBLE.',
    'The Weeknd': 'Blinding Lights'
}

# Print the entire dictionary
print("Artist Songs Dictionary:", artist_songs)

# Access and print the top song of the 3rd artist
print("Top song of the third artist (Ed Sheeran):", artist_songs['Ed Sheeran'])

# Update the top song of the 6th artist
artist_songs['Beyoncé'] = 'Crazy in Love'
print("Updated top song of the sixth artist (Beyoncé):", artist_songs['Beyoncé'])

# Delete the 7th artist from the dictionary
del artist_songs['Kendrick Lamar']
print("Dictionary after deleting the 7th artist:", artist_songs)

# Print the last key-value pair in the dictionary
last_key = list(artist_songs.keys())[-1]
print("Last key-value pair:", last_key, ":", artist_songs[last_key])
