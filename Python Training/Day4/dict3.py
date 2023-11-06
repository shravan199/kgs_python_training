
d= {'name': 'shravan', 'age': 20, 'MobNo.': 903554304, 94545: '454544dfsf', 
    'name': 'sdfds', 5454:5444554, (9, 23.60): '45'}

items = d.items()

print(items)

print()
keys, values = [], []

for (key, value) in d.items():
    keys.append(key)
    values.append(value)

print(f'Keys are: {keys}, Type of it is: {type(keys)}')
print(f'Values are: {values}, Type of it is: {type(values)}')