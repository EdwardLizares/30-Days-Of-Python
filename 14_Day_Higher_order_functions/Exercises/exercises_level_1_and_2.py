print("""1:
    Map uses a function on all items
    Filter uses a filter function (T/F) and removes items that return False
    Reduce uses a reduction function to merge all items together
""")

print("""2:
    Higher Order functions return other functions
    Closures remember variables from outer functions after they've already finished (?)
    Decorators are functions that transform other functions
""")


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("4:", countries)
print("5:", names)
print("6:", numbers)

# Level 2
def upper(x):
    return x.upper()
upper_countries = map(upper, countries)
print("1:", list(upper_countries))

def square(x):
    return x**2
squared_numbers = map(square, numbers)
print("2:", list(squared_numbers))

upper_names = map(upper, names)
print("3:", list(upper_names))

def land(x):
    return "land" in x
land_countries = filter(land, countries)
print("4:", list(land_countries))

def len_six(x):
    return len(x) == 6
six_countries = filter(len_six, countries)
print("5:", list(six_countries))

print("6:", list(filter(lambda x: len(x)>=6, countries)))
print("7:", list(filter(lambda x: x[0] == 'E', countries)))

# skip 8

def get_string_lists(l):
    return list(filter(lambda x: type(x) == str, l))
print("9:", get_string_lists([1,2,"This", "works", 3, 4]))

from functools import reduce
print("10:", reduce(lambda x, y: x+y, numbers))

print("11:", reduce(lambda x,y: x+" "+y, countries))

def categorize_countries(p):
    return list(filter(lambda x: p in x, countries))
print("12:", categorize_countries("land"))

def letter_count():
    res = {}
    for c in countries:
        if c[0] not in res: 
            res[c[0]] = 0
        res[c[0]] += 1
    return res
print("13:", letter_count())

# skip 14-15

# no decorators or closures practice? 