dic = {'name': 'Suresh', 'age': 24, 89:'test', 'email_id': 'suresh@gmail.com', 
       98.89 : 'xyz', ('user_name', 'pwd'): ('suresh123', 'suresh@123'),
         89: 'test2'}
        
# How to retrive data from dict
# print(dic[892])

value= dic.get(89, 'Key doesn\'t exist in specified dict.')
print(value, type(value))


# How to get all the keys
keys = dic.keys()
print(f'Keys: {keys} and type of keys: {type(keys)}')

keys= []
for key in dic.keys():
    keys.append(key)

print(keys, type(keys))

# retrieve all the vlaues from dict
dict_values = dic.values()
print(dict_values)


# how to retrieve key and value at time from dict
print()
dict_kvp = dic.items()
print(dict_kvp)

print()
for key,value in dic.items():
    print(f'{key}:{value}')


