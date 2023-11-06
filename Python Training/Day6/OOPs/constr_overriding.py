class Father:
    def __init__(self, fname) -> None:
        self.fname = fname

    def gardening(self):
        print("I enjoy gardening")

    def skills(self):
        print("Father class Skill mehtod: I enjoy gardening", self.fname)

class Mother(Father):
    def __init__(self, mname, fname) -> None:
        self.mname = mname
        super().__init__(fname)

    def cooking(self):
        print("I love cooking")
    
    def skills(self):
        print("Mother class Skill mehtod: I enjoy cooking", self.mname)

class Child(Mother):
    def __init__(self, cname, mname, fname) -> None:
        self.cname = cname
        super().__init__(mname, fname)
        print(f'cname: {self.cname}')

    def  skills(self):
        # Mother.skills(self)
        # Father.skills(self)
        print("I enjoy sports", self.cname)

child1 =Child(cname='shravan', mname='Nirmala', fname='Ram Bhavan Jha')
child1.skills()
# child1.gardening()
# child1.cooking()
Mother.skills(child1) # Method overriding
Father.skills(child1)