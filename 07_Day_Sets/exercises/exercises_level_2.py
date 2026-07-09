A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A_B = A.union(B)
print("1:", A_B)
A_x_B = A.intersection(B)
print("2:", A_x_B)
print("3:", A.issubset(B))
print("4:", len(A_x_B) == 0) # or use isdisjoint
A_w_B = B.union(A)
B_w_A = A.union(B)
print("5:", A_w_B, B_w_A)
print(A.symmetric_difference(B))
del A
del B
