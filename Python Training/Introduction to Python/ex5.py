a = ('SHRAVAN', 2, 4, 7, (5, 6), [9, 8])
print(a, type(a), id(a))
b = ('SHRAVAN', 2, 4, 7, (5, 6), [9, 8])
print(b, type(b), id(b))

print(a==b)

print(id(a) == id(b))

# Reverse element using silicing in python
c = a[::-1]
print(f'Reversed container is: {a[::-1]}')
name = "shravan kumar jha"
print(f'{name[::-1]}')