num = input('Input a number: ')

result = 1
if num.isdigit():
    num = int(num)
    if num ==0 or num ==1:
        print(result)
    else:
        for num in range(1, num+1):
            result *= num
        print(result)
else:
    print(f'Please enter a valid positive number.')