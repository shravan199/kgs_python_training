class details:
    i=0
    print("This is details class.")
    def __init__(self):
        details.i+=1
        print("this is init method.and object No.",self.i)
        
obj1=details()#1
obj2=details()#1
print(obj1.i)
print(obj2.i)