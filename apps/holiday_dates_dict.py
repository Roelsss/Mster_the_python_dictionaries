# Create a dictionary of 10 holidays and their corresponding dates
holiday_dates = {
    'New Year': 'January 1',
    'Valentine\'s Day': 'February 14',
    'Easter': 'April 9',
    'Independence Day': 'July 4',
    'Halloween': 'October 31',
    'Thanksgiving': 'November 23',
    'Christmas': 'December 25',
    'Labor Day': 'September 4',
    'Mother\'s Day': 'May 14',
    'Father\'s Day': 'June 18'
}

# Print the entire dictionary
print("Holiday Dates Dictionary:", holiday_dates)

# Access and print the date of the 4th holiday
print("Date of the fourth holiday:", holiday_dates['Independence Day'])

# Update the date of the 9th holiday
holiday_dates['Mother\'s Day'] = 'May 21'
print("Updated date of the ninth holiday:", holiday_dates['Mother\'s Day'])

# Delete the 2nd holiday from the dictionary
del holiday_dates['Valentine\'s Day']
print("Dictionary after deleting the 2nd holiday:", holiday_dates)

# Print the last key-value pair in the dictionary
last_key = list(holiday_dates.keys())[-1]
print("Last key-value pair:", last_key, ":", holiday_dates[last_key])
