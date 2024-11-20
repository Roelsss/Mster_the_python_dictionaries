# Create a dictionary of 8 flowers and their symbolic meanings
flower_meanings = {
    'Rose': 'Love',
    'Lily': 'Purity',
    'Sunflower': 'Adoration',
    'Tulip': 'Perfect Love',
    'Daffodil': 'Rebirth',
    'Orchid': 'Beauty',
    'Cherry Blossom': 'Fleeting Beauty',
    'Carnation': 'Devotion'
}

# Print the entire dictionary
print("Flower Meanings Dictionary:", flower_meanings)

# Access and print the meaning of the 5th flower
print("Meaning of the fifth flower:", flower_meanings['Daffodil'])

# Update the meaning of the 7th flower
flower_meanings['Cherry Blossom'] = 'Renewal'
print("Updated meaning of the seventh flower:", flower_meanings['Cherry Blossom'])

# Delete the 6th flower from the dictionary
del flower_meanings['Orchid']
print("Dictionary after deleting the 6th flower:", flower_meanings)

# Print the last key-value pair in the dictionary
last_key = list(flower_meanings.keys())[-1]
print("Last key-value pair:", last_key, ":", flower_meanings[last_key])
