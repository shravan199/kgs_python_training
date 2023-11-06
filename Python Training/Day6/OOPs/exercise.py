class Car:

    def __init__(self, name, type, price) -> None:
        self.name = name
        self.type = type
        self.price= price
        print(f'Name: {self.name}, Type: {self.type}, Price: {self.price}')

car1 = Car('Fer', 'Red Conv.', 545454.44)
car2 = Car('Jump', 'Blue Ven.', 565656.44)

        