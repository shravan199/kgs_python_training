class Father:
    def gardening(self):
        print("I enjoy gardening")

    def skills(self):
        print("Father class Skill mehtod: I enjoy gardening")

class Mother(Father):
    def cooking(self):
        print("I love cooking")
    
    def skills(self):
        print("Mother class Skill mehtod: I enjoy cooking")

class Child(Mother):
    def  skills(self):
        Mother.skills(self)
        Father.skills(self)
        print("I enjoy sports")

child1 =Child()
child1.skills()
# child1.gardening()
# child1.cooking()
Mother.skills(child1) # Method overriding
Father.skills(child1)