import random
import string 
from exercises_level_1 import rgb_color_gen

def list_of_hexa_colors(n):
    return ["#"+"".join(random.choices(string.digits+"ABCDEF", k=6)) for i in range(n)]

def list_of_rgb_colors(n):
    return [rgb_color_gen() for i in range(n)]

def generate_colors(t, n):
    if t == 'hexa':
        return list_of_hexa_colors(n)
    else:
        return list_of_rgb_colors(n)

if __name__ == "__main__":
    print(generate_colors('hexa', 3))