b=[1,1.2,"Test",(45,78),1,1,1,1,1,1,1,1]
a=set(b)
# a={1,1.2,"Test",(45,78)}
print(a)
print(id(a),type(a),len(a))
a.add(45)
a.discard(1.2)
print(a)
print(id(a),type(a),len(a))

for i in a:
    print(i)
