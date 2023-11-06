class details:
#     i=0
    print("This is details class.")
    def __init__(self,name,email,mobileNo):
        print("this is init method.and object No.")
        self.name=name 
        self.email=email 
        self.mobileNo=mobileNo
        
    def __str__(self):
        return f"{self.name} {self.email} and {self.mobileNo}"
        
obj1=details("Nishant","Test@gmail.com",896646)
print(obj1)
obj2=details("Raj","Test1234@gmail.com",57898954)
print(obj2)