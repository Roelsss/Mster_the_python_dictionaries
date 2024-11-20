# Create a dictionary of 6 software programs and their latest versions
software_versions = {
    'Windows 11': '22H2',
    'macOS Ventura': '13.0',
    'Ubuntu': '22.04 LTS',
    'Android 14': '14.0',
    'iOS 17': '17.0',
    'Chrome': '118.0.5993.116'
}

# Print the entire dictionary
print("Software Versions Dictionary:", software_versions)

# Access and print the version of the 4th software
print("Version of the fourth software (Android 14):", software_versions['Android 14'])

# Update the version of the 2nd software
software_versions['macOS Ventura'] = '13.1'
print("Updated version of the second software (macOS Ventura):", software_versions['macOS Ventura'])

# Delete the 5th software from the dictionary
del software_versions['iOS 17']
print("Dictionary after deleting the 5th software:", software_versions)

# Print the last key-value pair in the dictionary
last_key = list(software_versions.keys())[-1]
print("Last key-value pair:", last_key, ":", software_versions[last_key])
