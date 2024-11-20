# Create a dictionary of 10 festivals and their celebration dates
festival_dates = {
    'New Year': 'January 1',
    'Christmas': 'December 25',
    'Diwali': 'November 12',
    'Eid al-Fitr': 'April 21',
    'Halloween': 'October 31',
    'Thanksgiving': 'November 28',
    'Holi': 'March 25',
    'Valentine\'s Day': 'February 14',
    'Easter': 'April 9',
    'Oktoberfest': 'September 16'
}

# Print the entire dictionary
print("Festival Dates Dictionary:", festival_dates)

# Access and print the date of the 3rd festival
print("Date of the third festival (Diwali):", festival_dates['Diwali'])

# Update the date of the 7th festival
festival_dates['Holi'] = 'March 20'
print("Updated date of the seventh festival (Holi):", festival_dates['Holi'])

# Delete the 5th festival from the dictionary
del festival_dates['Halloween']
print("Dictionary after deleting the 5th festival:", festival_dates)

# Print the last key-value pair in the dictionary
last_key = list(festival_dates.keys())[-1]
print("Last key-value pair:", last_key, ":", festival_dates[last_key])
