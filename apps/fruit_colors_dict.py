# Create a dictionary of 8 fruits and their corresponding colors
fruit_colors = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Orange': 'Orange',
    'Grapes': 'Purple',
    'Lemon': 'Yellow',
    'Blueberry': 'Blue',
    'Peach': 'Pink',
    'Watermelon': 'Green'
}

# Print the entire dictionary
print("Fruit Colors Dictionary:", fruit_colors)

# Access and print the color of the 6th fruit
print("Color of the sixth fruit:", fruit_colors['Blueberry'])

# Update the color of the 4th fruit
fruit_colors['Grapes'] = 'Green'
print("Updated color of the fourth fruit:", fruit_colors['Grapes'])

# Delete the 7th fruit from the dictionary
del fruit_colors['Peach']
print("Dictionary after deleting the 7th fruit:", fruit_colors)

# Print the last key-value pair in the dictionary
last_key = list(fruit_colors.keys())[-1]
print("Last key-value pair:", last_key, ":", fruit_colors[last_key])
