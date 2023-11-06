def details(firstname="Jk",lastname="Tata",age=16):
    global name
    name=firstname+' '+lastname #func var > local
    return name,age,out

out="Hello" # script var > global
v=details('Manish',age=78,lastname="Meena")
print(v)
print(name)