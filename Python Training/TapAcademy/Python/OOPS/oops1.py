class Car:
    def __init__(self) -> None:
        self.brand = 'BMW'
        self.cc = 2100
        self.color = 'Blue'

    def start_engine(self):
        print(f'{self.brand} engine is starting.')

def main():
    c1 = Car() ## __new__() method will invoked
    print(c1.brand)
    print(c1.cc)
    print(c1.color)
    c1.start_engine() # internally it is like start_engine(c1)

print(f'Value of magical varable __name__: {__name__}')
if __name__ == '__main__':
    main()