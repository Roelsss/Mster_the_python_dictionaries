# Create a dictionary of 8 foods and their recipes
food_recipes = {
    'Spaghetti': 'Boil pasta, sauté garlic in olive oil, mix with tomato sauce, add basil.',
    'Pizza': 'Prepare dough, spread sauce, add cheese and toppings, bake at 450°F for 10-15 minutes.',
    'Tacos': 'Warm tortillas, fill with seasoned meat, add lettuce, cheese, and salsa.',
    'Burger': 'Grill beef patty, toast bun, add lettuce, tomato, cheese, and sauce.',
    'Fried Rice': 'Cook rice, stir-fry with vegetables, soy sauce, scrambled egg, and protein.',
    'Salad': 'Toss mixed greens, cucumber, tomatoes, olive oil, and balsamic vinegar.',
    'Soup': 'Boil vegetables in broth, season with salt, pepper, and herbs.',
    'Pancakes': 'Mix flour, milk, eggs, and baking powder, cook on a hot griddle, serve with syrup.'
}

# Print the entire dictionary
print("Food Recipes Dictionary:", food_recipes)

# Access and print the recipe of the 5th food
print("Recipe of the 5th food (Fried Rice):", food_recipes['Fried Rice'])

# Update the recipe of the 3rd food
food_recipes['Tacos'] = 'Warm tortillas, fill with grilled chicken, add avocado, lettuce, and salsa.'
print("Updated recipe of the 3rd food (Tacos):", food_recipes['Tacos'])

# Delete the 7th food from the dictionary
del food_recipes['Soup']
print("Dictionary after deleting the 7th food (Soup):", food_recipes)

# Print the last key-value pair in the dictionary
last_key = list(food_recipes.keys())[-1]
print("Last key-value pair:", last_key, ":", food_recipes[last_key])
