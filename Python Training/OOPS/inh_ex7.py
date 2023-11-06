# multiple inheritance in python 
#method overriding
#error
#Solve the method overloading  prob.
class Father:
    def __init__(self,fname):
        self.fname=fname
    def skills(self):
        print("I enjoy gardening",self.fname)

class Mother(Father):
    def __init__(self,mname):
        
        self.mname=mname
    def skills(self):
        print("I love cooking",self.mname)

class Child(Mother,Father):
    def __init__(self,name,mname,fname): 
        self.name=name
    def  skills(self):
        Mother.skills(self)
        Father.skills(self)#when method overriding is there
        print("I enjoy sports",self.name)
        
c=Child('me',"Maa","Paa")
c.skills()