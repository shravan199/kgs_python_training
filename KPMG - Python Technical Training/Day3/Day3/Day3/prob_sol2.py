a=input("Enter the value b/w 0-20:-")
print(a,len(a))
a=a.strip() 
if a.isdigit():
    a=int(a)
    if 0<=a<=20:
        fact=1
        for i in range(1,a+1): # 1:2:1 >1
            print(f"{i}*{fact}=",end='')
            fact=fact*i 
            print(fact)
        print(f"The factorial of the value {a} is {fact}")
    else:
        print(f"Enterd value:- {a},out of range(0<{a}>20) .")
else:
    print(f"Enterd value:- {a}, Note:- Please Enter the valid Integer Number b/w 0-20.")