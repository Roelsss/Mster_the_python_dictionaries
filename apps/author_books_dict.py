# Create a dictionary of 8 authors and their famous books
author_books = {
    'J.K. Rowling': 'Harry Potter and the Sorcerer\'s Stone',
    'George Orwell': '1984',
    'J.R.R. Tolkien': 'The Lord of the Rings',
    'F. Scott Fitzgerald': 'The Great Gatsby',
    'Harper Lee': 'To Kill a Mockingbird',
    'Jane Austen': 'Pride and Prejudice',
    'Mark Twain': 'Adventures of Huckleberry Finn',
    'Ernest Hemingway': 'The Old Man and the Sea'
}

# Print the entire dictionary
print("Author Books Dictionary:", author_books)

# Access and print the book of the 5th author
print("Book of the 5th author (Harper Lee):", author_books['Harper Lee'])

# Update the book of the 7th author
author_books['Mark Twain'] = 'The Adventures of Tom Sawyer'
print("Updated book of the 7th author (Mark Twain):", author_books['Mark Twain'])

# Delete the 6th author from the dictionary
del author_books['Jane Austen']
print("Dictionary after deleting the 6th author:", author_books)

# Print the last key-value pair in the dictionary
last_key = list(author_books.keys())[-1]
print("Last key-value pair:", last_key, ":", author_books[last_key])
