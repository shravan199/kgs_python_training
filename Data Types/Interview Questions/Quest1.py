dict1 = {'name': 'Suresh', 'age': 23, 'age': 25, 98: 'age', 87.67: 98.533,
         ('uname', 'pwd'): ['suresh10', 'suresh@123']}

print(f'dict1: {dict1}, length: {len(dict1)}')

for k,v in dict1.items():
    print(f'{k}: {v}')

dict2 = {}
print(f'dict2: {dict2}, length: {len(dict2)}')