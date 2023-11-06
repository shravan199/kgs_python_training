class Vehicle:
    var = 78
    def general_use(self):
        print(f'Vehicle: Used for transportation')

class Car(Vehicle):
    def  __init__(self) -> None:
        self.no_of_wheels =4
        self.has_roof = True
        print(f'Car has {self.no_of_wheels} wheels. It also having roof {self.has_roof}')

    def specific_use(self):
        print(f'Inside class: {self.var}')
        print(f'Car is used to commute office. We can travel with family')


car1 = Car()
car1.specific_use()
car1.general_use()
print(f'Outside class: {car1.var}')