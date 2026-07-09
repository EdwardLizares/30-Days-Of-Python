def add_two_numbers(a, b):
    return a+b

def area_of_circle(r):
    return 3.14*r**2

def add_all_nums(*args):
    res = 0
    for i in args:
        if not isinstance(i, (int, float)):
            return "Not all arguments are numbers"
        res += i
    return res

def convert_celsius_to_fahrenheit(c):
    return c*9/5+32

# skip 5-15

