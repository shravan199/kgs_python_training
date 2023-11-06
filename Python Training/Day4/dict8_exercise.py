family_dict = {}
for i in range(1, 6):
    name= input(f'Enter the {i} name: ')
    age = input(f'Enter the {name}\'s age: ')
    if not age.isdigit():
        print(f'Please enter valid age')
        age = input(f'Enter the {name}\'s age: ')

    family_dict[name] = int(age)

print(family_dict)
print()
# get key by value
while True:
    in_age = input(f'Please enter age: ')
    if not in_age.isdigit():
        print(f'Please enter valid age')
        in_age = input(f'Please enter age: ')

    in_age = int(in_age)

    for key, value in family_dict.items():      
        if in_age == value:
            print(f'User {name} belongs to age: {age}')
        else:
            print(f'Not found match try again.')
