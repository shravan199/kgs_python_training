
txt = '''
Food Menu:
 1. Burger
 2. Pizza
 3. Tomato Soup
'''
price = (30, 100, 40)

print(txt)
choice = int(input('Enter your choice: '))
qty = int(input('Enter quantity: '))

amount_withoutTax = qty * price[choice-1]
total_amount = amount_withoutTax * 1.05
tax = total_amount - amount_withoutTax
output = f'''
 Tax = {tax}
 Total amount = {total_amount}
 Thank you. Visit again!
'''

print(output)