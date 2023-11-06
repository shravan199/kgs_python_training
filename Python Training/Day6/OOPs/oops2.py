class DemoClass:
    var = 90
    print(f'This is demo class')
    
print(f'print from class memory: {DemoClass.var}')

obj = DemoClass()
print(f'print from object memory: {obj.var}')

print(f'Print class varable DemoClass: {DemoClass}')
print(f'Address of DemoClass: {id(DemoClass)}')

obj.var +=20
print(obj.var)

print(f'Print obj instance: {obj}')
print(f'Address of obj: {id(obj)}')
obj2 = DemoClass()
print(f'Obj2: {obj2.var}')
print(f'Print obj2 instance: {obj2}')
print(f'Address of obj2: {id(obj2)}')

DemoClass.var +=30
print(f'Democlass variable increased by 30: {DemoClass.var}')