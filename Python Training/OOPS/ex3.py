class demo:
    var = 78
    print('This is dmeo class.')

    def moxicip(self, name='Krishna', age=90):
        print('This is moxicip method.')
        name1 = name + ' '+ 'Sharma'
        return name1, age, self.var


# create object
print('\n***********Object 1************')
obj1 = demo()
print(obj1)
obj1.var += 20
print(obj1.var)
v= obj1.moxicip('Raj', 45)
print(v)

print('\n***********Object 2************')
obj2 = demo()
print(obj2)
obj2.var += 30
print(obj2.moxicip(age=56, name='Manish'))

print('\n***********Object 3************')
obj3 = demo()
obj3.var -= 15
print(obj3)
print(obj3.moxicip())