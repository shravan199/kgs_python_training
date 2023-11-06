class Vehicle:
    def general_usage(self):
        print("general use: transporation")

class Car:
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        
        print("specific use: commute to work, vacation with family")

class MotorCycle:
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        
        print("specific use: road trip, racing")