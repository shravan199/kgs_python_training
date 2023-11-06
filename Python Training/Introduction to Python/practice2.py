
num = input('Enter a number btw 0 and 100: ')
print(f'user enterted {num}, {type(num)}, {len(num)}')

try:
    num = float(num)
    if num <= 100:
        if num > 10 and num < 60:
            if num > 43:
                print(f'The value {num} is large')
            elif num < 35 and num >= 43:
                print(f'The value {num} is medium')
            else:
                print(f'The value {num} is small')
        else:
            print(f'Value is not between 10 and 60')
    else:
        print(f'Value {num} is out of range  means > 100')
except ValueError as ve:
    print(f'Please enter valid number')
except Exception as ex:
    print(f'Error is: {ex}')
