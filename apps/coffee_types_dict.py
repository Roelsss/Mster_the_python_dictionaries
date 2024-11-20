# Create a dictionary of 10 types of coffee and their descriptions
coffee_types = {
    'Espresso': 'A strong, black coffee brewed by forcing steam through finely ground coffee beans.',
    'Americano': 'Espresso with hot water added, resulting in a similar strength to regular drip coffee.',
    'Latte': 'Espresso mixed with steamed milk and topped with a small amount of milk foam.',
    'Cappuccino': 'Espresso with steamed milk and a thick layer of milk foam, often sprinkled with cocoa or cinnamon.',
    'Macchiato': 'Espresso with a small amount of steamed milk or milk foam.',
    'Mocha': 'A chocolate-flavored variant of a latte, made with espresso, steamed milk, and chocolate syrup.',
    'Flat White': 'Espresso with steamed milk and a velvety smooth texture, with less foam than a cappuccino.',
    'Affogato': 'A dessert coffee made by pouring a shot of hot espresso over a scoop of vanilla ice cream.',
    'Ristretto': 'A shorter, more concentrated version of espresso, made with less water.',
    'Cortado': 'Equal parts espresso and steamed milk, creating a smooth and balanced flavor.'
}

# Print the entire dictionary
print("Coffee Types Dictionary:", coffee_types)

# Access and print the description of the 4th type of coffee
print("Description of the 4th type of coffee (Cappuccino):", coffee_types['Cappuccino'])

# Update the description of the 8th type of coffee
coffee_types['Affogato'] = 'A delicious dessert coffee made with hot espresso poured over a scoop of vanilla ice cream.'
print("Updated description of the 8th type of coffee (Affogato):", coffee_types['Affogato'])

# Delete the 5th type of coffee from the dictionary
del coffee_types['Macchiato']
print("Dictionary after deleting the 5th type of coffee:", coffee_types)

# Print the last key-value pair in the dictionary
last_key = list(coffee_types.keys())[-1]
print("Last key-value pair:", last_key, ":", coffee_types[last_key])
