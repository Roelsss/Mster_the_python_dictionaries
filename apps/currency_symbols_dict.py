# Create a dictionary of 10 currencies and their symbols
currency_symbols = {
    'USD': '$',
    'EUR': '€',
    'GBP': '£',
    'JPY': '¥',
    'AUD': 'A$',
    'CAD': 'C$',
    'INR': '₹',
    'CHF': 'Fr',
    'CNY': '¥',
    'MXN': '$'
}

# Print the entire dictionary
print("Currency Symbols Dictionary:", currency_symbols)

# Access and print the symbol of the 5th currency
print("Symbol of the fifth currency:", currency_symbols['AUD'])

# Update the symbol of the 9th currency
currency_symbols['CNY'] = '元'
print("Updated symbol of the ninth currency:", currency_symbols['CNY'])

# Delete the 3rd currency from the dictionary
del currency_symbols['GBP']
print("Dictionary after deleting the 3rd currency:", currency_symbols)

# Print the last key-value pair in the dictionary
last_key = list(currency_symbols.keys())[-1]
print("Last key-value pair:", last_key, ":", currency_symbols[last_key])
