class DemoClass:
    var = 90
    print('This is demo class.')


obj1= DemoClass()
print(obj1.var)
obj1.var += 20
print(f'Value of var in object 1: {obj1.var}') 
obj2 = DemoClass()
print(f'Value of var in object 2: {obj2.var}')
print(DemoClass.var)

