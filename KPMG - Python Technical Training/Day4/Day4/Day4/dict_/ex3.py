d=dict(name="Nishant",age=89,dept="L&D",_888878="Test")
print(d)
print(id(d),type(d),len(d))

d1={"one":1,"two":{"username":"Test","password":"2133"}}
print(d1)
print(id(d1),type(d1),len(d1))

print("========update dict==================")
#update an existing key , value 
d['name']="Sanjay"
#update and add new pair with an existing dict object
d["Data"]="t3624"
#update dict d with pairs of dict d1 
d.update(d1)
#clear the dict object
d.clear()
print(d)
print(id(d),type(d),len(d))
##########################
#create dict d3 with pairs of d1 and d ,Note without any change in d and d1 dict.
#======3 line============
#d3=
#======2 lines============
#d3=
#======1 line============
#d3=
print(d3)
print(id(d3),type(d3),len(d3))



