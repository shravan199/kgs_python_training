def details(firstname='test', lastname='sdfs', age=89):
    global name
    name=firstname+' '+lastname 
    return name,age,out


v=details("Manish", age= 56, lastname='Meena')
out='hello'
print(v)
print(name)

