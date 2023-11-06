# how to ceate dictionay in python
# key1: value1, key2: value2 .... and so on
dic = {'name': 'Suresh', 'age': 24, 89:'test', 'email_id': 'suresh@gmail.com', 
       98.89 : 'xyz', ('user_name', 'pwd'): ('suresh123', 'suresh@123'),
         89: 'test2'}

print(f'type: {type(dic)}, address: {id(dic)}, no_pairs: {len(dic)}')

# how to read/get itmes from dict
for key, value in dic.items():
    print(f'key: {key} and vlaue : {value}')

# key1 = value1, key2= value2 ... so on
dic2 = dict(name='Mahesh', age = 34, email_id = 'mahesh@gmail.com', _89 = 'age', _89='age2')

print(f'############ Another way to create dict ################')

print(f'type: {type(dic2)}, address: {id(dic2)}, no_pairs: {len(dic2)}')

# how to read/get itmes from dict
for key, value in dic2.items():
    print(f'key: {key} and vlaue: {value}')