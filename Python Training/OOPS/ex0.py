class DemoClass:
    x=90
    print ('THis is demo class')
    print('this is demo class 2')

    def test_method(self):
        print('this is test_method inside class')


    def __init__(self):
        print('I am init method')    



obj1 = DemoClass()
obj1.x += 20
print(obj1.x)
print(DemoClass.x)
obj1.test_method()