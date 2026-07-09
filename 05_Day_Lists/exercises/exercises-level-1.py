empy_list = []
print("1:", empy_list)
list_2 = [1,2,3,4,5,6]
print("2:", list_2)
print("3:", len(list_2))
print("4:", list_2[0], list_2[len(list_2)//2], list_2[-1])
mixed_data_types = ['Edward', 25, 1.75, 'Signle', 'House']
print("5:", mixed_data_types)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("6&7:", it_companies)
print("8:", len(it_companies))
print("9:", it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])
it_companies[0] = 'Meta'
print("10:", it_companies)
it_companies.append('Twitter')
print("11:", it_companies)
it_companies.insert(3, 'Tesla')
print("12:", it_companies)
it_companies[0] = it_companies[0].upper()
print("13:", it_companies)
print("14:", '#; '.join(it_companies))
print("15:", 'Facebook' in it_companies)
it_companies.sort()
print("16:", it_companies)
it_companies.sort(reverse=True)
print("17:", it_companies)
print("18:", it_companies[:3])
print("19:", it_companies[-3:])
print("20:", it_companies[len(it_companies)//2])
it_companies.pop(0)
print("21:", it_companies)
it_companies.pop(len(it_companies)//2)
print("22:", it_companies)
it_companies.pop(-1)
print("23:", it_companies)
it_companies.clear()
print("24:", it_companies)
del it_companies
print("it_companies" in locals())  
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print("26:", full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print("27:", full_stack)
