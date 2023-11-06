class demo:
    var = 78 # public
    __var1 = 90 #private
    _var2=100 # protected
#    name1=None
    print("This is demo class")

    def moxicip(self, name="Krishna", age=90):
        print("This is moxicip method.")
        name1 = name+' '+"Sharma"  # local
        self.name1 = name1  # create an object attribute name1
        return name1, age, self.var  # object memory #demo.var#class memory

    def out(self):
        #         v=self.moxicip()#get the method moxicip() with in another method
        print(self.name1)  # get the attribute value from the object


obj1 = demo()
print(f'Public attribute: {obj1.var}')
obj1.var +=10
print(f'Public attribute: {obj1.var}')

print(f'Protected attribute: {obj1._var2}')
obj1._var2 +=10
print(f'Protected attribute: {obj1._var2}')
print(f'print private variable __var2 using class variable {demo._var2}')
print(f'Private attribute: {obj1.__var1}')
