print("1:", "Thirty" + "Days" + "Of" + "Python")
print("2:", "Coding" + "For" + "All")

company = "Coding For All"
print("3&4:", company)

print("5:", len(company))
print("6:", company.upper())
print("7:", company.lower())
print("8:", company.capitalize(), company.title(), company.swapcase())
print("9:", company[7:])
print("10:", company.find("Coding")!=-1)
print("11:", company.replace("Coding", "Python"))
print("12:", "Python For Everyone".replace("Everyone", "All"))
print("13:", company.split())
print("14:", "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
print("15:", company[0])
print("16:", len(company)-1)
print("17:", company[10])
print("18:", "".join(i[0] for i in "Python For Everyone".split()))
print("19:", "".join(i[0] for i in "Coding For All".split()))
print("20:", company.index("C"))
print("21:", company.index("F"))
print("22:", "Coding For All People".rfind("l"))
because = 'You cannot end a sentence with because because because is a conjunction'
print("23:", because.find("because"))
print("24:", because.rfind("because"))
print("25:", because.replace("because because because ", ""))

# 26-27 duplicate

print("28:", "Coding For All".startswith("Coding"))
print("29:" "Coding For All".endswith("Coding"))
print("30:", "   Coding For All      ".strip())
print("31:", "30DaysOfPython".isidentifier(), "thirty_days_of_python".isidentifier())
print("32:", " # ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print("33:", "I am enjoying this challenge. \n I just wonder what is next.")
print("34:", "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2

print("35:", f"The area of a circle with radius {radius} is {area} meters square.")

# skip 36