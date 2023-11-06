# loop it 5 times with for loop 
for i in range(5):
    a=input("Enter the value 0-100:-")
    if a.isdigit():
        a=int(a)
        if 0<=a<=100: #101
            if 10<a<60:
                if a>43:
                    print(f"The Value {a} is Large.")
                elif a>35 and a<=43:
                    print(f"The Value {a} is Medium.")
                else:
                    print(f"The Value {a} is Small.")
                
            else:
                print(f"The Value {a} out of Range(10<value<60) . ")
        else:
            print(f"Value {a} Out of range(0-100)")
    else:
        print("Please Enter the valid Integer Number b/w 0-100.")