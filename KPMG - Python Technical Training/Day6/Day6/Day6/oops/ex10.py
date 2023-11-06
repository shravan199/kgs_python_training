# multilevel inheritance in python
#method overriding
#method overloading 
class Father:
    def __init__(self,fname):
        self.fname=fname
    def skills(self):
        print("I enjoy gardening",self.fname)

class Mother(Father):
    def __init__(self,mname,fname):
        super().__init__(fname)
        self.mname=mname
    def skills(self):
        print("I love cooking",self.mname)

class Child(Mother):
    def __init__(self,name,mname,fname):
        super().__init__(mname, fname)
        self.name=name
    def  skills(self):
        Father.skills(self)#when method overriding is there
        Mother.skills(self)
        print("I enjoy sports",self.name)
        
c=Child('me',"Maa","Paa")
c.skills()