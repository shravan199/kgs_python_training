class UserDetail:
    print(f'This is user detial class')

    # constr
    def __init__(self, name, email, mob_no):
        self.name = name
        self.email = email
        self.mob_no = mob_no
        print(f'User details:-\n Name is: {self.name} \
              \n Email is: {self.email} and \n Mobile Number is: {self.mob_no}')
        
    def __str__(self):
        return self.name

user1 = UserDetail('Shravan', 'skhad@gmail.com', 4656565656)
print(user1)
print()
user2 = UserDetail('Shreyansh', 'skhad@gmail.com', 4656565656)
print(user2)

