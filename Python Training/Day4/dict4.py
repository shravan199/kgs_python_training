d=dict(name="Nishant",age=89,dept="L&D",_888878="Test")
print(d)
print(id(d),type(d),len(d))
print()

d1={"one":1,"two":{"username":"Test","password":"2133"}}
print(d1)
print(id(d1),type(d1),len(d1))
print()

# update dictionary value

d['name'] = 'Shravan'

print(d)
print(id(d),type(d),len(d))
print()

#update and add new pair with an existing dict object
d['email_id'] = 'sdfsd@gmaild.com'

print(d)
print(id(d),type(d),len(d))
print()


d.update(d1)
print(d)
print(id(d),type(d),len(d))
print()


#clear the dict
d.clear()
print(d)
print(id(d),type(d),len(d))
print()
