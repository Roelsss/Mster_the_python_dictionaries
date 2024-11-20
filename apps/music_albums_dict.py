# Create a dictionary of 10 music albums and their release years (updated with more recent albums)
music_albums = {
    'Folklore': 2020,  # Taylor Swift
    'Future Nostalgia': 2020,  # Dua Lipa
    'After Hours': 2020,  # The Weeknd
    'DAMN.': 2017,  # Kendrick Lamar
    'Lover': 2019,  # Taylor Swift
    '1989': 2014,  # Taylor Swift
    'Starboy': 2016,  # The Weeknd
    'In the Heights Soundtrack': 2021,  # Various artists (soundtrack)
    'Chemtrails over the Country Club': 2021,  # Lana Del Rey
    'Lover': 2019  # Taylor Swift
}

# Print the entire dictionary
print("Music Albums Dictionary:", music_albums)

# Access and print the release year of the 3rd album
print("Release year of the third album (After Hours):", music_albums['After Hours'])

# Update the release year of the 8th album
music_albums['In the Heights Soundtrack'] = 2020
print("Updated release year of the eighth album (In the Heights Soundtrack):", music_albums['In the Heights Soundtrack'])

# Delete the 5th album from the dictionary
del music_albums['Lover']
print("Dictionary after deleting the 5th album:", music_albums)

# Print the last key-value pair in the dictionary
last_key = list(music_albums.keys())[-1]
print("Last key-value pair:", last_key, ":", music_albums[last_key])
