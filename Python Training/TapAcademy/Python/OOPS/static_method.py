class BmwCar:
    def __init__(self, name, cc, color) -> None:
        self.name = name
        self.cc = cc
        self.color= color

    @staticmethod
    def kms_to_miles(kms):
        print(f'{kms* 1.6 } miles')

def main():
    car = BmwCar('BMW 200', 2000, 'blue')
    BmwCar.kms_to_miles(2)
    car.kms_to_miles(2)

if __name__ == '__main__':
    main()