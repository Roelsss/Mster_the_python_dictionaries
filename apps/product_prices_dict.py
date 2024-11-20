# Create a dictionary of 10 products and their prices with updated items
product_prices = {
    'Electric Kettle': 60,
    'Blender': 120,
    'Toaster': 50,
    'Microwave': 150,
    'Washing Machine': 400,
    'Refrigerator': 800,
    'Dishwasher': 650,
    'Coffee Maker': 100,
    'Air Purifier': 200,
    'Vacuum Cleaner': 250
}

# Print the entire dictionary
print("Product Prices Dictionary:", product_prices)

# Access and print the price of the 4th product
print("Price of the fourth product (Microwave):", product_prices['Microwave'])

# Update the price of the 9th product
product_prices['Air Purifier'] = 210
print("Updated price of the ninth product (Air Purifier):", product_prices['Air Purifier'])

# Delete the 6th product from the dictionary
del product_prices['Refrigerator']
print("Dictionary after deleting the 6th product:", product_prices)

# Print the last key-value pair in the dictionary
last_key = list(product_prices.keys())[-1]
print("Last key-value pair:", last_key, ":", product_prices[last_key])
