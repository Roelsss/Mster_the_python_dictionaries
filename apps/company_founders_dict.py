# Create a dictionary of 8 companies and their founders
company_founders = {
    'Apple': 'Steve Jobs',
    'Microsoft': 'Bill Gates',
    'Google': 'Larry Page & Sergey Brin',
    'Amazon': 'Jeff Bezos',
    'Tesla': 'Elon Musk',
    'Facebook': 'Mark Zuckerberg',
    'SpaceX': 'Elon Musk',
    'Twitter': 'Jack Dorsey'
}

# Print the entire dictionary
print("Company Founders Dictionary:", company_founders)

# Access and print the founder of the 6th company
print("Founder of the sixth company (Facebook):", company_founders['Facebook'])

# Update the founder of the 2nd company
company_founders['Microsoft'] = 'Bill Gates & Paul Allen'
print("Updated founder of the second company (Microsoft):", company_founders['Microsoft'])

# Delete the 8th company from the dictionary
del company_founders['Twitter']
print("Dictionary after deleting the 8th company:", company_founders)

# Print the last key-value pair in the dictionary
last_key = list(company_founders.keys())[-1]
print("Last key-value pair:", last_key, ":", company_founders[last_key])
