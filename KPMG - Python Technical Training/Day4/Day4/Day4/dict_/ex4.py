d=dict(name="Nishant",age=89,dept="L&D",_888878="Test")
print(d)
print(id(d),type(d),len(d))
print("========delete dict==================")
# del d["name1"]
#to get the deleted value also handle the exception
key= '_888878'
f=d.pop(key,"Key Not found!")
if f=="Key Not found!":
    print(f"key < {key} >:-",f)
else:
    print(f"Deleted value of key < {key} >:-",f)
print(d)
print(id(d),type(d),len(d))

g=d.copy() 
print(g)
print(id(g))