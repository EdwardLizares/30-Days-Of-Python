def is_prime(n):
    # opimal only check until sqrt n
    if n<=3:
        return True
    for i in range(2,int(n**0.5)+1):
        if (n/i)%1 == 0:
            return f"Divisible by {i}"
    return f"{n} is a prime!"

def all_unique(l):
    return len(l) == len(set(l))

def same_types(l):
    types = set()
    for i in l:
        types.add(type(i))
    return len(types) == 1
test = [1, 2, 3, "4"]

def valid_variable(v):
    return v.isidentifier()

# skip 5

if __name__ == "__main__":
    print(valid_variable("test"))