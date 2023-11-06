#positional arguments
def details(firstname,lastname,age):
    name=firstname+' '+lastname 
    return name,[age]

v=details('Manish',"Meena",78)
print(v)

m=details("Raj", "Sharma", 67)
print(m)