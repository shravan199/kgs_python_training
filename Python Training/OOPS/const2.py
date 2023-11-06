class Vehicle:
    def __init__(self,name,type,price):
        print(f"{name} is a {type} worth {price}$.") 
           
car1=Vehicle("Fer","Red cov.",734483490)
car2=Vehicle("Jump","Blue Van" ,463676)
###########################################
class Vehicle:
    def get_data(self,name,type,price):
        print(f"{name} is a {type} worth {price}$.") 
           
car1=Vehicle()
car1.get_data("Fer","Red cov.",734483490)
car2=Vehicle()
car2.get_data("Jump","Blue Van" ,463676)