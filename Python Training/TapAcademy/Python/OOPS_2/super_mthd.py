class Customer:
    def __init__(self, name, mob_no, address):
        self.name = name
        self.mob_no = mob_no
        self.address = address

class  PlatetinumCustomer(Customer):
    def __init__(self, name, mob_no, address, plt_id):
        super().__init__(name, mob_no, address)
        self.plt_id = plt_id
    
    def display(self):
        print(self.__dict__)


def main():
    pc = PlatetinumCustomer('shravan', 900999, 'banglrore', 20)
    pc.display()


if __name__ == '__main__':
    main()