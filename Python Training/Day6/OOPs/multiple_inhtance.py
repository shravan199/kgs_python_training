class Father:
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def  skills(self):
        print("I enjoy sports")

child1 =Child()
child1.skills()
child1.gardening()
child1.cooking()