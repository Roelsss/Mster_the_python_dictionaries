# Create a dictionary of 8 movie genres and their corresponding example movies
movie_genres = {
    'Action': 'Die Hard',
    'Comedy': 'The Hangover',
    'Drama': 'The Shawshank Redemption',
    'Horror': 'The Conjuring',
    'Romance': 'The Notebook',
    'Thriller': 'Inception',
    'Sci-Fi': 'Interstellar',
    'Animated': 'Toy Story'
}

# Print the entire dictionary
print("Movie Genres Dictionary:", movie_genres)

# Access and print the example movie of the 3rd genre
print("Example movie of the third genre:", movie_genres['Drama'])

# Update the example movie of the 5th genre
movie_genres['Romance'] = 'Pride and Prejudice'
print("Updated example movie of the fifth genre:", movie_genres['Romance'])

# Delete the 7th genre from the dictionary
del movie_genres['Sci-Fi']
print("Dictionary after deleting the 7th genre:", movie_genres)

# Print the last key-value pair in the dictionary
last_key = list(movie_genres.keys())[-1]
print("Last key-value pair:", last_key, ":", movie_genres[last_key])
