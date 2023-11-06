num = int(input('Enter a positvie integer:'))


msg = 'BTM' if num%3 ==0 and num%5 == 0  else 'TAP' if num % 3 ==0 else 'Academy' if num%5 == 0 else None
print(msg)