a= [3, 5, 4, 6, 9, 8, 23]
print(a)
print(id(a),type(a),len(a))

a.reverse()
print(a)
print(id(a),type(a),len(a))

a = a[::-1]
print(a)
print(id(a),type(a),len(a))

a.sort()
print(a)
print(id(a),type(a),len(a))

a.sort(reverse=True)
print(a)
print(id(a),type(a),len(a))