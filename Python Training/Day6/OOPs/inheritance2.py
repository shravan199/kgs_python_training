class Vehicle:
    var = 78
    def general_use(self):
        print(f'Vehicle: Used for transportation')

class Car(Vehicle):
    var = 45
    def  __init__(self) -> None:
        print(f'I am car')
        self.no_of_wheels =4
        self.has_roof = True
        #print(f'Car has {self.no_of_wheels} wheels. It also having roof {self.has_roof}')

    def specific_use(self):
        print(f'Inside class: {self.var} and {Vehicle.var}')
        self.general_use()
        print(f'Car is used to commute office. We can travel with family')

class MotorCycle (Vehicle):
    var = 34
    def  __init__(self) -> None:
        print(f'I am MotorCycle')
        self.no_of_wheels =2
        self.has_roof = False
        #print(f'Car has {self.no_of_wheels} wheels. It also having roof {self.has_roof}')

    def specific_use(self):
        print(f'Inside class: {self.var} and {Vehicle.var}')
        self.general_use()
        print(f'MotorCycle is used to commute office only')

car1 = Car()
car1.specific_use()
car1.general_use()
print(f'Outside class: {car1.var} and {Vehicle.var}')

mc1 = MotorCycle()
mc1.specific_use()