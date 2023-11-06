a = [1, 2, 3, 4, 5]

print(a, len(a), type(a), id(a))

a[2] = 9
print(a, len(a), type(a), id(a))

a.append(8)
print(a, len(a), type(a), id(a))

a.append([3, 5])
print(a, len(a), type(a), id(a))

a.insert(3, 78)
print(a, len(a), type(a), id(a))

a.insert(5, ('test', 2.8))
print(a, len(a), type(a), id(a))

a.extend(('shravan', 'kr', 45, 3.5))
print(a, len(a), type(a), id(a))

del a[7]
print(a, len(a), type(a), id(a))

a.remove([3, 5])
print(a, len(a), type(a), id(a))

# m = a.pop()
# print(m)
# print(a, len(a), type(a), id(a))

m=  a.pop(-0)
print(m)
print(a, len(a), type(a), id(a))