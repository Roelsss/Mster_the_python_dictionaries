# Create a dictionary of 10 car brands and their country of origin
car_brands = {
    'Toyota': 'Japan',
    'Ford': 'USA',
    'BMW': 'Germany',
    'Chevrolet': 'USA',
    'Honda': 'Japan',
    'Mercedes-Benz': 'Germany',
    'Audi': 'Germany',
    'Tesla': 'USA',
    'Hyundai': 'South Korea',
    'Nissan': 'Japan'
}

# Print the entire dictionary
print("Car Brands Dictionary:", car_brands)

# Access and print the country of origin of the 3rd car brand
print("Country of origin of the third car brand:", car_brands['BMW'])

# Update the country of origin of the 7th car brand
car_brands['Audi'] = 'Germany (Updated)'
print("Updated country of origin of the seventh car brand:", car_brands['Audi'])

# Delete the 8th car brand from the dictionary
del car_brands['Tesla']
print("Dictionary after deleting the 8th car brand:", car_brands)

# Print the last key-value pair in the dictionary
last_key = list(car_brands.keys())[-1]
print("Last key-value pair:", last_key, ":", car_brands[last_key])
