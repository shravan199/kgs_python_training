from time import time as t

def odd_even(number=5):
    if number % 2 ==0:
        out = 'even'
    else:
        out = 'odd'
    fact= factorial(number)
    return out, number, fact

def factorial(number):
    fact =1
    if number == 0:
        return fact
    else:
        for i in range(1, number+1):
            fact *= i
        return fact
    

# value  =input('Enter the value:')
# if value.isdigit():
#     value = int(value)
# else:
#     print(f'Please enter valid integer')

# op= odd_even(value)
# print(f'Output is: {op}')