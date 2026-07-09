age = int(input("Enter age: "))
if (age >= 18):
    print("You are old enough to drive")
else:
    print(f"You need {18-age} more years to learn how to drive")

my_age = 25
your_age = int(input("Enter your age: "))

diff = abs(my_age - your_age)
if my_age < your_age:
    if diff == 1:
        print(f"You are {diff} year older than me")
    else:
        print(f"You are {diff} years older than me")
elif my_age > your_age:
    if diff == 1:
        print(f"You are {diff} year younger than me")
    else:
        print(f"You are {diff} years younger than me")
else:
    print("We the same age twin")

num_1 = int(input("Enter number one: "))
num_2 = int(input("Enter number two: "))
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
if num_1 < num_2:
    print(f"{num_1} is less than {num_2}")
else:
    print(f"{num_1} equals {num_2}")
