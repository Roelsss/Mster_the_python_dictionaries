# Create a dictionary of 12 books and their authors
book_authors = {
    'To Kill a Mockingbird': 'Harper Lee',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby-Dick': 'Herman Melville',
    'War and Peace': 'Leo Tolstoy',
    'The Catcher in the Rye': 'J.D. Salinger',
    'The Hobbit': 'J.R.R. Tolkien',
    'Ulysses': 'James Joyce',
    'Crime and Punishment': 'Fyodor Dostoevsky',
    'Brave New World': 'Aldous Huxley',
    'The Odyssey': 'Homer'
}

# Print the entire dictionary
print("Book Authors Dictionary:", book_authors)

# Access and print the author of the 9th book
print("Author of the ninth book:", book_authors['Ulysses'])

# Update the author of the 5th book
book_authors['Moby-Dick'] = 'Herman Melville (Updated)'
print("Updated author of the fifth book:", book_authors['Moby-Dick'])

# Delete the 3rd book from the dictionary
del book_authors['Pride and Prejudice']
print("Dictionary after deleting the 3rd book:", book_authors)

# Print the last key-value pair in the dictionary
last_key = list(book_authors.keys())[-1]
print("Last key-value pair:", last_key, ":", book_authors[last_key])
