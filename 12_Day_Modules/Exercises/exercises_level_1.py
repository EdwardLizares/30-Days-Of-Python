import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def user_id_gen_by_user():
    c = int(input())
    n = int(input())
    res = ""
    for i in range(n):
        res += ''.join(random.choices(string.ascii_letters + string.digits, k=c)) + "\n"
    return res

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rgb({r},{g},{b})"

if __name__ == "__main__":
    print(rgb_color_gen())