a=lambda x=10,y=5: x**2+y**2+2*x/y+56.89
print(a)
print(type(a))
#x=10 y=5
b=a(10,5)#positional argument
print(b)

b=a(y=5,x=10)#keyword argument
print(b)

b=a()
print(b)