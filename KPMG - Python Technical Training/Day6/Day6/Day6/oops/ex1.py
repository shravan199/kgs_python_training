class DemoClass:
    var=90#public
    print("This is Demo Class.")
    
    
   
obj1=DemoClass()#create a new object in python
print(obj1)
print(obj1.var)
obj1.var += 20 #update the value with in the obj1 Memory 
print(DemoClass.var)#take it back from the Class memory
print("=============Another Object-2=============")
obj2=DemoClass()
print(obj2)
print(obj2.var)
obj2.var +=10
print(obj1.var)
print(obj2.var)

    
    
