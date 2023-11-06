class DemoClass:
    var = 78
    print(f'This is demo class')

    def moxicip(self, name='Nirmala', age=34):
        name2 = name + ' Jha' # local scope
        self.name2=  name2 # create object level variable
        print(f'This is moxicip method')
        return f'{name2} is {age} years old. Value of var {self.var}'
    
    def out(self):
        self.moxicip()
        print(f'Print name: {self.name2}')

obj = DemoClass()
obj.var = 90
print(obj.var)

print(f'Democlass var : {DemoClass.var}')
# DemoClass.moxicip()
print(obj.moxicip('Shravan', 23))

obj2 = DemoClass()
obj2.var = 909
print(obj2.moxicip('Shreyesh', 2))

obj3 = DemoClass()

obj3.moxicip('jyoti', 25)
obj3.out()
print(obj3.name2)

obj2.out()