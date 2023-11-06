class Customer:
    def __init__(self, name, mob_no, address):
        self.name = name
        self.mob_no = mob_no
        self.address = address
    
    def place_oder(self, dish):
        del_charge=50
        cost = 0
        if dish == 'pizza':
            cost = 500 + del_charge
        else:
            cost = 250 + del_charge
        return cost

class  PlatinumCustomer(Customer):
    def __init__(self, name, mob_no, address, plt_id):
        super().__init__(name, mob_no, address)
        self.plt_id = plt_id
    
    def place_oder(self, dish):
        del_charge = 50
        return (super().place_oder(dish) - del_charge)*0.95

    def display(self):
        print(self.__dict__)

def main():
    pc = PlatinumCustomer('shravan', 900999, 'banglrore', 20)
    pc.display()
    print(pc.place_oder('pizza'))

if __name__ == '__main__':
    main()