print("1: ", end="")
for i in range(11):
    print(i, end="")

print("\n2: ", end="")
i = 0
while i < 11:
    print(i, end="")
    i += 1

print("\n3: ")
for i in range(7):
    print('#'*(i+1))
print("\n4: ")
for i in range(8):
    for j in range(8):
        print('#', end=" ")
    print("")

print("\n5: ")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

print("\n6: ")
for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(i)

print("\n7: ")
for i in range(100):
    if i%2 == 0:
        print(i, end=" ")

print("")
print("\n8: ")
for i in range(100):
    if i%2 == 1:
        print(i, end=" ")
