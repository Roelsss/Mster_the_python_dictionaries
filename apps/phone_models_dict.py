# Create a dictionary of 10 phone models and their manufacturers
phone_models = {
    'iPhone 15': 'Apple',
    'Galaxy S23': 'Samsung',
    'Pixel 8': 'Google',
    'OnePlus 11': 'OnePlus',
    'Xperia 1 IV': 'Sony',
    'Nokia G50': 'Nokia',
    'Motorola Edge 40': 'Motorola',
    'iPhone 14': 'Apple',
    'Galaxy Z Fold 5': 'Samsung',
    'Google Pixel 7': 'Google'
}

# Print the entire dictionary
print("Phone Models Dictionary:", phone_models)

# Access and print the manufacturer of the 2nd phone model
print("Manufacturer of the second phone model (Galaxy S23):", phone_models['Galaxy S23'])

# Update the manufacturer of the 8th phone model
phone_models['iPhone 14'] = 'Apple Inc.'
print("Updated manufacturer of the eighth phone model (iPhone 14):", phone_models['iPhone 14'])

# Delete the 6th phone model from the dictionary
del phone_models['Nokia G50']
print("Dictionary after deleting the 6th phone model:", phone_models)

# Print the last key-value pair in the dictionary
last_key = list(phone_models.keys())[-1]
print("Last key-value pair:", last_key, ":", phone_models[last_key])
