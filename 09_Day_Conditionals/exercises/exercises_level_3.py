person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])//2])
    print('Python' in person['skills'])
    if set(person['skills']) == set(['JavaScript', 'React']):
        print("He is a front end developer")
    elif set(['Node', 'Python', 'MongoDB']).issubset(set(person['skills'])):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']).issubset(set(person['skills'])):
        print('He is a full stack')
    else:
        print('unkown title')

if person['is_married'] and (person['country'] == 'Finland'):
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married")