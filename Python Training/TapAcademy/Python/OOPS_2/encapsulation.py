class AccountHolder:
    def __init__(self):
        self.__bal = 10000

    @property
    def bal(self):
        print('get_bal() called.')
        return self.__bal
    
    @bal.setter
    def bal(self, amt):
        print('set_bal() called.')
        if amt >= 0:
            self.__bal = amt
        else:
            print(f'Invalid amount: {amt}. Please enter valid amount.')

    # bal = property(get_bal, set_bal)   

def main():
   
   ah = AccountHolder()
   print(ah.bal)
   ah.bal = -2000
   print(ah.bal)

if __name__== '__main__':
    main()