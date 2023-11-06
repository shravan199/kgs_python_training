class demo:
    var=78
    print("This is demo class")

    def moxicip(self,name="Krishna",age=90):
        print("This is moxicip method.")
        name1=name+' '+"Sharma" #local
        self.name1= name1 #"Test Value" # create an object attribute name1
        return name1,age,self.var #object memory #demo.var #class memory
    
    def out(self):
        self.moxicip()
        print(self.name1)
    
obj1=demo()
print(obj1.moxicip())
obj1.out()
# print(demo.name1)

obj2 = demo()
#obj2.moxicip(age=56, name= 'shravan')
obj2.out()