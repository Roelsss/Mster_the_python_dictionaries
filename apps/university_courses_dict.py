# Create a dictionary of 8 universities and their popular courses
university_courses = {
    'Harvard University': 'Business Administration',
    'Stanford University': 'Computer Science',
    'Massachusetts Institute of Technology': 'Engineering',
    'University of Oxford': 'Law',
    'University of Cambridge': 'Medicine',
    'California Institute of Technology': 'Physics',
    'University of Chicago': 'Economics',
    'Princeton University': 'Mathematics'
}

# Print the entire dictionary
print("University Courses Dictionary:", university_courses)

# Access and print the course of the 3rd university
print("Course of the third university:", university_courses['Massachusetts Institute of Technology'])

# Update the course of the 5th university
university_courses['University of Cambridge'] = 'Data Science'
print("Updated course of the fifth university:", university_courses['University of Cambridge'])

# Delete the 7th university from the dictionary
del university_courses['University of Chicago']
print("Dictionary after deleting the 7th university:", university_courses)

# Print the last key-value pair in the dictionary
last_key = list(university_courses.keys())[-1]
print("Last key-value pair:", last_key, ":", university_courses[last_key])
