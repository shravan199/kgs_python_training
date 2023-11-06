class Details:
    i = 0
    print(f'This is details class')

    def __init__(self):
        Details.i +=2
        print(f'This is __init__ method constructor. Object number: {self.i}')

obj = Details()
obj2 = Details()
print(obj.i)
print(obj2.i)