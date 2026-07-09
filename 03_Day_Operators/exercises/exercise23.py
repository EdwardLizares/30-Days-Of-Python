matrix = [[1*((j+1)**i) for i in range(4)] for j in range(5)]
for row in range(5):
    print(str(row+1), "".join([str(i)+" " for i in matrix[row]]))