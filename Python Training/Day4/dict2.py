d = {2, }
d2= {'name': 'shravan', 'age': 20, 'MobNo.': 903554304, 94545: '454544dfsf', 
    'name': 'sdfds', 5454:5444554, (9, 23.60): '45'}

# d = dict(key1 = value1, key2 = value2 ......) here Key should be identifier
d = dict(name = 'shravan', age=30, _9909='dsfsdfdfdeeee')
print(f'Dict: {d}')
print(f'Type: {type(d)}, Address: {id(d)} and Length: {len(d)}')

# get the value from dictionary
value = d['_9909']
print(value)

v2 = d.get('nam3e', 'Key not found')
print(v2)

key3 = (92, 23.60)
v3 = d2.get(key3, f'Key {key3} not found')

print(v3)

# loop using keys
for key in d2:
    print(key)

values = d2.values()
print(values, type(values))

for value in d2.values():
    print(value)

values2= []

for value in d2.values():
    values2.append(value)

print(f'Values are: {values2}, Type of it is: {type(values2)}')
print(values2[2])


keys = d2.keys()
print(keys, type(keys))

keys2= []

for key in d2.keys():
    keys2.append(key)

print(f'Keys are: {keys2}, Type of it is: {type(keys2)}')
print(keys2[2])