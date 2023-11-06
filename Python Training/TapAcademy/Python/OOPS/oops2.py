class FootBolwer:
    def __init__(self, name, team, goals) -> None:
         self.name = name
         self.team = team
         self.goals = goals

    def shooting(self):
         print(f'{self.name} is shooting')
    
    def passing(self):
         print(f'{self.name} is passing')

    def running(self):
         print(f'{self.name} is running')

    def display(self):
         print(f'Name: {self.name}, Team: {self.team}, Goals: {self.goals}, \
               Age: {self.age}, Jersy_No: {self.jersey_no}')
         

def main():
    cr = FootBolwer('Cristiano', 'Juventus', 746)
    #     cr.age = 34
    #     cr.jersey_no = 7
    setattr(cr, 'age', 35)
    setattr(cr, 'jersey_no', 7)
    cr.display()
    
    print(cr.__dict__)
    print(cr.name)
    print(cr.__dict__['name'])
#     messi = FootBolwer('Messi', 'Barcelona', 700)
#     messi.age = 36
#     messi.jersey_no =22
#     messi.display()

if __name__ == '__main__':
     main()