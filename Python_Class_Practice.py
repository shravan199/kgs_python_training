import requests

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


class Person:
  name = 'defaul name'
  age= 'defaul age'
  mob_num= 'defaul mob num'
  email= 'defaul email'
   
  def __init__(self, name, age, mob_num, email):
    self.name = name
    self.age = age
    self.mob_num = mob_num
    self.email = email
    
  # this fun is not working
  def print_detail():
    print('Name is:' + self.name + 'Age is:' + self.age + 'Mob no. is: '+ self.mob_num + \
          'Email is: ' + self.email)
      
  
shravan = Person( 'Shravan', 25, 9454464535, 'skjha898@gmail.com')
print()
print(shravan.name)
print(shravan.age)
print(shravan.mob_num)
print(shravan.email)
    
  
    
    
    
  
  
  
