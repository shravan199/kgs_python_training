"""
this module about 
fact_1
odd_even
time 

etc
"""

import time as t

def fact_1(n):
    """
    hello
    """
    from math import factorial 
    fact=factorial(n)
    return n,fact


def odd_even(number=5):
    if number%2==0:
        out="Even"
        jk=fact_1(number)
    else:
        out="Odd"
        jk=fact_1(number)
    return out,number,jk[1]


# print("==========I am running from bounce.py ==========")
# value=input("Enter the value:-")
# if value.isdigit():
#     value=int(value)
#     var=odd_even(value)
#     print(f"The value {var[1]} is {var[0]} and factorial is {var[2]}")
# else:
#     print("Invalid Input.")
#     var=odd_even()
#     print(f"The value {var[1]} is {var[0]} and factorial is {var[2]}")
    
        