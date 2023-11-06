class Vehicle:
    var=78
    def general_usage(self):
        print("general use: transporation")
        
#simple inheritance
class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Inside class:-",self.var)
        print("specific use: commute to work, vacation with family")

c=Car()
print(c.has_roof)
c.specific_usage()
c.general_usage()
print("outside class:-",c.var)