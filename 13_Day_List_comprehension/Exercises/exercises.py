numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print("1:", [i for i in numbers if i <= 0])

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = lambda x, y, z: x + y + z
print("2:", l(*list_of_lists))

print([j+[1*j[0]**k for k in range(6)] for j in [[i] for i in range(11)]])
# i just realized how much i over complicated this
# pattern is that the 2nd column is just first columns ^ 0, I did it like
# first column is the column id kinda, then the next columns go from 1 to the column 
# number 1*rowid**column_num. but i could've just done 0->5

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("4:", [[i[0][0].upper(), i[0][0][:3].upper(), i[0][1].upper()] for i in countries])

print("5:", [{'country': i[0][0].upper(), 'city': i[0][1].upper()} for i in countries])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print("6:", [" ".join(i[0]) for i in names])

# skip 7