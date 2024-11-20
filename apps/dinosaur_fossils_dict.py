# Create a dictionary of 7 dinosaurs and where their fossils were found
dinosaur_fossils = {
    'Tyrannosaurus Rex': 'North America',
    'Triceratops': 'North America',
    'Velociraptor': 'Mongolia',
    'Brachiosaurus': 'Tanzania',
    'Stegosaurus': 'North America',
    'Spinosaurus': 'North Africa',
    'Allosaurus': 'North America'
}

# Print the entire dictionary
print("Dinosaur Fossils Dictionary:", dinosaur_fossils)

# Access and print the location of the 4th dinosaur's fossils
print("Location of the 4th dinosaur (Brachiosaurus) fossils:", dinosaur_fossils['Brachiosaurus'])

# Update the location of the 2nd dinosaur's fossils
dinosaur_fossils['Triceratops'] = 'Western United States'
print("Updated location of the 2nd dinosaur (Triceratops) fossils:", dinosaur_fossils['Triceratops'])

# Delete the 6th dinosaur from the dictionary
del dinosaur_fossils['Spinosaurus']
print("Dictionary after deleting the 6th dinosaur:", dinosaur_fossils)

# Print the last key-value pair in the dictionary
last_key = list(dinosaur_fossils.keys())[-1]
print("Last key-value pair:", last_key, ":", dinosaur_fossils[last_key])
