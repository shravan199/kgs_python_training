# multilevel inheritance in python
#method overriding
class Father:
    def skills(self):
        print("I enjoy gardening")

class Mother(Father):
    def skills(self):
        print("I love cooking")

class Child(Mother):
    def  skills(self):
#         Father.skills(self)#when method overriding is there
#         Mother.skills(self)
        print("I enjoy sports")
        
c=Child()
c.skills()
#How to access the Method skills of Mother class  
#with child class object c when method overriding is there? 
# Mother.skills(c)
# Father.skills(c)
