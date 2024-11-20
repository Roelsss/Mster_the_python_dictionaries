# Create a dictionary of 8 cities and their famous landmarks
city_landmarks = {
    'Paris': 'Eiffel Tower',
    'New York': 'Statue of Liberty',
    'Rome': 'Colosseum',
    'London': 'Big Ben',
    'Sydney': 'Sydney Opera House',
    'Tokyo': 'Tokyo Tower',
    'Moscow': 'Red Square',
    'Cairo': 'Pyramids of Giza'
}

# Print the entire dictionary
print("City Landmarks Dictionary:", city_landmarks)

# Access and print the landmark of the 6th city
print("Landmark of the sixth city (Tokyo):", city_landmarks['Tokyo'])

# Update the landmark of the 2nd city
city_landmarks['New York'] = 'Empire State Building'
print("Updated landmark of the second city (New York):", city_landmarks['New York'])

# Delete the 7th city from the dictionary
del city_landmarks['Moscow']
print("Dictionary after deleting the 7th city:", city_landmarks)

# Print the last key-value pair in the dictionary
last_key = list(city_landmarks.keys())[-1]
print("Last key-value pair:", last_key, ":", city_landmarks[last_key])
