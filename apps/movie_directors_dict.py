# Create a dictionary of 10 movies and their directors
movie_directors = {
    'Inception': 'Christopher Nolan',
    'Titanic': 'James Cameron',
    'The Shawshank Redemption': 'Frank Darabont',
    'The Godfather': 'Francis Ford Coppola',
    'The Dark Knight': 'Christopher Nolan',
    'Schindler\'s List': 'Steven Spielberg',
    'The Lord of the Rings: The Fellowship of the Ring': 'Peter Jackson',
    'The Matrix': 'Lana and Lilly Wachowski',
    'Pulp Fiction': 'Quentin Tarantino',
    'Fight Club': 'David Fincher'
}

# Print the entire dictionary
print("Movie Directors Dictionary:", movie_directors)

# Access and print the director of the 5th movie
print("Director of the fifth movie:", movie_directors['The Dark Knight'])

# Update the director of the 9th movie
movie_directors['Pulp Fiction'] = 'Quentin Tarantino (Updated)'
print("Updated director of the ninth movie:", movie_directors['Pulp Fiction'])

# Delete the 7th movie from the dictionary
del movie_directors['The Lord of the Rings: The Fellowship of the Ring']
print("Dictionary after deleting the 7th movie:", movie_directors)

# Print the last key-value pair in the dictionary
last_key = list(movie_directors.keys())[-1]
print("Last key-value pair:", last_key, ":", movie_directors[last_key])
