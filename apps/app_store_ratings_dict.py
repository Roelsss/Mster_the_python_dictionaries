# Create a dictionary of 10 apps and their user ratings
app_store_ratings = {
    'Instagram': 4.5,
    'TikTok': 4.7,
    'WhatsApp': 4.6,
    'Facebook': 4.2,
    'YouTube': 4.8,
    'Spotify': 4.4,
    'Snapchat': 4.3,
    'Twitter': 4.1,
    'LinkedIn': 4.3,
    'Pinterest': 4.6
}

# Print the entire dictionary
print("App Store Ratings Dictionary:", app_store_ratings)

# Access and print the rating of the 6th app
print("Rating of the sixth app:", app_store_ratings['Spotify'])

# Update the rating of the 8th app
app_store_ratings['Twitter'] = 4.2
print("Updated rating of the eighth app:", app_store_ratings['Twitter'])

# Delete the 9th app from the dictionary
del app_store_ratings['LinkedIn']
print("Dictionary after deleting the 9th app:", app_store_ratings)

# Print the last key-value pair in the dictionary
last_key = list(app_store_ratings.keys())[-1]
print("Last key-value pair:", last_key, ":", app_store_ratings[last_key])
