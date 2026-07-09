from exercises_level_1 import family_members

print(f"Family members: {family_members}")

sibling_1, sibling_2, sibling_3, sibling_4, *parents = family_members
print("1:", sibling_1, sibling_2, sibling_3, sibling_4, parents)

fruits = ('strawberry', 'banana', 'mango')
vegetables = ('onion', 'garlic')
animal_products = ('milk', 'steak')
food_stuff_tp = fruits + vegetables + animal_products
print("2:", food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print("3:", food_stuff_lt)
print("4:", food_stuff_tp[4])
print("5:", food_stuff_lt[:3] + food_stuff_lt[-3:])
del food_stuff_tp
try:
    print(food_stuff_tp)
except:
    print("6: food_stuff_tp was deleted.")

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("7:", 'Estonia' in nordic_countries, 'Iceland' in nordic_countries)