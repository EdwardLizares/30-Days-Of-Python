def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n+1):
        if i%2==0:
            evens+=1
        else:
            odds+=1
    return f"The number of odds are {odds}\nThe number of evens are {evens}"

def factorial(n):
    f = 1 # factorial(0) is 1
    for i in range(1, n+1):
        f*=i
    return f

def is_empty(p):
    if isinstance(p, (list, dict, set, tuple)):
        return len(p) == 0
    else:
        return "Not a Container"
test = []

# skip 4-6

if __name__ == "__main__":
    print(is_empty(test))