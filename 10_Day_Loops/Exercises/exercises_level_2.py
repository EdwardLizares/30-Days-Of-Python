sum = 0
for i in range(101):
    sum += i
print(f"The sum of all numbers is f{sum}")

sum_even = 0
sum_odd = 0
for i in range(101):
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of all evens is {sum_even}. And the sum of all odds is f{sum_odd}.")
