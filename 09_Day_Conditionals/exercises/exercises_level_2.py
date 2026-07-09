score = int(input("Enter score: "))
grades = ['A', 'B', 'C', 'D', 'F']
score -= 60
grade = 4
while (score >= 0):
    score -= 10
    grade -= 1
print(f"Your grade is: {grades[grade]}")

month = input("Enter month: ")
seasons = {
    'September': 'Autumn',
    'October': 'Autumn',
    'November': 'Autumn',
    'December': 'Winter',
    'January': 'Winter',
    'February': 'Winter',
    'March': 'Spring',
    'April': 'Spring',
    'May': 'Spring',
    'June': 'Summer',
    'July': 'Summer',
    'August': 'Summer'
}
print(seasons[month])

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter fruit: ")
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print(fruits)