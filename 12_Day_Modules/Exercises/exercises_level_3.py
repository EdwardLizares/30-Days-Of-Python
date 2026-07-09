import random

def shuffle_list(l):
    random.shuffle(l)
    return l

def seven_random():
    unique = [i for i in range(10)]
    shuffle_list(unique)
    return unique[2:]

if __name__ == "__main__":
    print(seven_random())