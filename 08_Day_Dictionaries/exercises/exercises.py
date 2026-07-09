cat = {}
print("1:", cat)
cat.update({'name': 'Kaloy', 'color': 'black', 'breed': 'Persian', 'legs': 4, 'age': 1})
print("2:", cat)
student = {
    'first_name': "Edward",
    'last_name': "Lizares",
    'gender': "Male",
    'age': 23,
    'marital_status': 'Single',
    'skills': ["Volleyball"],
    'country': "Philippines",
    'city': "City",
    'address': "Home"
}
print("3:", student)
print("4:", len(student))
print("5:", student['skills'], type(student['skills']))
student['skills'].append('Videogames')
print("6:", student['skills'])
print("7:", student.keys())
print("8:", student.values())
student_ls = list(student.items())
print("9:", student_ls)
student.pop('address')
print("10:", student)
del student
