# Create a dictionary of 7 programming languages and their developers
programming_languages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C': 'Dennis Ritchie',
    'Ruby': 'Yukihiro Matsumoto',
    'JavaScript': 'Brendan Eich',
    'PHP': 'Rasmus Lerdorf',
    'Swift': 'Chris Lattner'
}

# Print the entire dictionary
print("Programming Languages Dictionary:", programming_languages)

# Access and print the developer of the 4th programming language
print("Developer of the fourth programming language:", programming_languages['Ruby'])

# Update the developer of the 6th programming language
programming_languages['PHP'] = 'The PHP Group'
print("Updated developer of the sixth programming language:", programming_languages['PHP'])

# Delete the 2nd programming language from the dictionary
del programming_languages['Java']
print("Dictionary after deleting the 2nd programming language:", programming_languages)

# Print the last key-value pair in the dictionary
last_key = list(programming_languages.keys())[-1]
print("Last key-value pair:", last_key, ":", programming_languages[last_key])
