import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

count = {}
regex_pattern = r' |\. '
for i in re.split(regex_pattern, paragraph):
    if i not in count:
        count[i] = 0
    count[i] += 1
print("1:", max(count, key=count.get))

text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regex_pattern = r'-?\d+'
points = re.findall(regex_pattern, text)
print("2:", points)
sorted_points = sorted([int(i) for i in points])
print("2:", sorted_points)
print("2:", max(sorted_points) - min(sorted_points))