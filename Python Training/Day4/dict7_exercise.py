family_dict = {}
for i in range(1, 6):
    name= input(f'Enter the {i} name: ')
    age = input(f'Enter the {name}\'s age: ')
    if not age.isdigit():
        print(f'Please enter valid ineger number')
        age = input(f'Enter the {name}\'s age: ')

    family_dict[name] = int(age)

print()
for item in family_dict.items():
    print(item)

print(family_dict)