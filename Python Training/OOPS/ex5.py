class demo:
    var=78
#    name1=None
    print("This is demo class")
    def moxicip(self,name="Krishna",age=90):
        print("This is moxicip method.")
        name1=name+' '+"Sharma"#local
        self.name1=name1#create an object attribute name1
        return name1,age,self.var#object memory #demo.var#class memory
    
    def out(self):
#         v=self.moxicip()#get the method moxicip() with in another method
        print(self.name1)#get the attribute value from the object
    
                
obj1=demo()
print(obj1)
print(obj1.var)
v=obj1.moxicip("Raj",45)
print(v)
obj1.out()
print(obj1.name1)

print(demo.name1)