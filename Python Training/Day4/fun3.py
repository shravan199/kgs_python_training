#keyword arguments
def details(firstname, lastname, age):
    name=firstname+' '+lastname 
    return name,age

v=details("Manish", 56, lastname='Meena')
print(v)

m=details("Raj", lastname="Sharma",age=67)
print(m)
