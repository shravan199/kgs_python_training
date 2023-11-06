d=dict(name="Nishant",age=89,dept="L&D",_888878="Test")
d1={"one":1,"two":{"username":"Test","password":"2133"}}
#create dict d3 with pairs of d1 and d ,Note without any change in d and d1 dict.
#======3 line============
d3= {}
d.update(d1)
for (key, value) in d.items():
    d3[key] = value

#======2 lines============
# d.update(d1)
# d3=d
#======1 line============
#d3=
print(d3)
print(id(d3),type(d3),len(d3))