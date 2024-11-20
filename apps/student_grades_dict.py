# Create a dictionary of 5 students and their grades
student_grades = {
    'Student1': 'B',
    'Student2': 'C',
    'Student3': 'A',
    'Student4': 'B+',
    'Student5': 'D'
}

# Print the entire dictionary
print("Student Grades Dictionary:", student_grades)

# Access and print the grade of the 3rd student
print("Grade of third student:", student_grades['Student3'])

# Update the grade of the 2nd student
student_grades['Student2'] = 'A'
print("Updated Grade of second student:", student_grades['Student2'])

# Delete the entry of the 5th student
del student_grades['Student5']
print("Dictionary after deleting 5th student:", student_grades)

# Print the last key-value pair in the dictionary
last_key = list(student_grades.keys())[-1]
print("Last key-value pair:", last_key, ":", student_grades[last_key])
