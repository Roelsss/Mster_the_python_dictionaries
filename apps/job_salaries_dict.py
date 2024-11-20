# Create a dictionary of 10 jobs and their average salaries
job_salaries = {
    'Software Engineer': 120000,
    'Data Scientist': 110000,
    'Product Manager': 95000,
    'Graphic Designer': 60000,
    'Teacher': 50000,
    'Doctor': 200000,
    'Nurse': 75000,
    'Architect': 85000,
    'Construction Worker': 45000,
    'Marketing Manager': 95000
}

# Print the entire dictionary
print("Job Salaries Dictionary:", job_salaries)

# Access and print the salary of the 3rd job
print("Salary of the 3rd job (Product Manager):", job_salaries['Product Manager'])

# Update the salary of the 7th job
job_salaries['Nurse'] = 80000
print("Updated salary of the 7th job (Nurse):", job_salaries['Nurse'])

# Delete the 9th job from the dictionary
del job_salaries['Construction Worker']
print("Dictionary after deleting the 9th job:", job_salaries)

# Print the last key-value pair in the dictionary
last_key = list(job_salaries.keys())[-1]
print("Last key-value pair:", last_key, ":", job_salaries[last_key])
