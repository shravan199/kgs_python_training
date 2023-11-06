d=dict(name="Nishant",age=89,dept="L&D",_888878="Test")
print(d)
print(id(d),type(d),len(d))

#del d["_888878"]

key= '_888878'
dlt_value = d.pop(key,f'<{key}> not found')

print(f'deleted value "{dlt_value}"')
print(d)
print(id(d),type(d),len(d))

g = d.copy()
print(g)
print(id(g),type(g),len(g))
