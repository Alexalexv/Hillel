users = [{'name': 'Luarvik L. Luarvik', 'age': 17},
         {'name': 'Olaf Andvarafors', 'age': 18},
         {'name': 'Brun Du Barnstokr', 'age': 19}]

names = []
for i in users:
    if i['age'] >= 18:
        names.append(i['name'])

print(names)
