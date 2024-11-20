# Create a dictionary of 8 festivals and their locations
festival_locations = {
    'Coachella': 'Indio, California, USA',
    'Glastonbury': 'Pilton, Somerset, England',
    'Burning Man': 'Black Rock City, Nevada, USA',
    'Tomorrowland': 'Boom, Belgium',
    'Lollapalooza': 'Chicago, Illinois, USA',
    'Montreux Jazz Festival': 'Montreux, Switzerland',
    'Rock in Rio': 'Rio de Janeiro, Brazil',
    'Sónar Festival': 'Barcelona, Spain'
}

# Print the entire dictionary
print("Festival Locations Dictionary:", festival_locations)

# Access and print the location of the 4th festival
print("Location of the 4th festival (Tomorrowland):", festival_locations['Tomorrowland'])

# Update the location of the 6th festival
festival_locations['Montreux Jazz Festival'] = 'Montreux, Switzerland (New Location)'
print("Updated location of the 6th festival (Montreux Jazz Festival):", festival_locations['Montreux Jazz Festival'])

# Delete the 2nd festival from the dictionary
del festival_locations['Glastonbury']
print("Dictionary after deleting the 2nd festival (Glastonbury):", festival_locations)

# Print the last key-value pair in the dictionary
last_key = list(festival_locations.keys())[-1]
print("Last key-value pair:", last_key, ":", festival_locations[last_key])
