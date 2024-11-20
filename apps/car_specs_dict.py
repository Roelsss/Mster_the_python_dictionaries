# Create a dictionary of 10 car models and their engine specifications
car_specs = {
    'Tesla Model S': 'Electric, 1020 hp, Dual Motor',
    'Ford Mustang': '5.0L V8, 450 hp, RWD',
    'Chevrolet Camaro': '6.2L V8, 455 hp, RWD',
    'BMW M3': '3.0L I6, 473 hp, AWD',
    'Audi A8': '3.0L V6, 333 hp, AWD',
    'Mercedes-Benz S-Class': '4.0L V8, 496 hp, AWD',
    'Porsche 911': '3.0L Twin-Turbo I6, 379 hp, AWD',
    'Nissan GT-R': '3.8L V6 Twin-Turbo, 565 hp, AWD',
    'Toyota Supra': '3.0L I6, 335 hp, RWD',
    'Honda Civic Type R': '2.0L I4 Turbo, 306 hp, FWD'
}

# Print the entire dictionary
print("Car Specifications Dictionary:", car_specs)

# Access and print the specifications of the 4th car model
print("Specifications of the fourth car model (BMW M3):", car_specs['BMW M3'])

# Update the specifications of the 9th car model
car_specs['Toyota Supra'] = '3.0L I6, 382 hp, RWD'
print("Updated specifications of the ninth car model (Toyota Supra):", car_specs['Toyota Supra'])

# Delete the 5th car model from the dictionary
del car_specs['Audi A8']
print("Dictionary after deleting the 5th car model:", car_specs)

# Print the last key-value pair in the dictionary
last_key = list(car_specs.keys())[-1]
print("Last key-value pair:", last_key, ":", car_specs[last_key])
