d={"name":"Nishant","Age":67,("Dept","others"):"l&D",
   98575.67:"hdbv#55625632bhvdsgh"}
print(d)
print(id(d),type(d),len(d))
print("==========Get the value from dict object============")
# f=d[("Dept","others1")]
# f=d.get(98575.67,"Key not matched!")
# print(f)
# 
# for i in d:
#     print(i)#return the keys

h=d.items()#d.keys()#d.values()
print(h)
print(type(h))

values=[]
keys=[]
for key,value in h:

    values.append(value)
    keys.append(key)
      
print("Values:- ",values)
print("Keys:-",keys)










    
