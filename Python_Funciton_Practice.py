def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_fun(*fruits):
  print('I like ' + fruits[2])
  
my_fun('banana', 'apple', 'grapes')


def my_function():
  print("Hello from a function")

my_function()


def my_fun(name):
  print('How are you ' + name + '?')
  
my_fun('shravan')
my_fun('jyoti')
my_fun('shreyansh')

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def print_result(data):
  print()
  for out in data:
    print(out)
    
data=[pl for pl in ['java', 'c#', '.net', 'javaScript'] if 'a' in pl]
print_result(data)
