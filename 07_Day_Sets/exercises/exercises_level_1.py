it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print("1:", len(it_companies))
it_companies.add('Twitter')
print("2:", it_companies)
it_companies.update(['LinkedIn', 'Snapchat'])
print("3:", it_companies)
it_companies.remove('IBM')
print("4:", it_companies)
print("Remove returns an error when the item is not in the set,\nbut discard doesn't")
