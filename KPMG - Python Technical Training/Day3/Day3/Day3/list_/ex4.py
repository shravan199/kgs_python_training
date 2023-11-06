a=["Test",1,1.2,(1,2),[89,67],56.6]
print(a)
print(id(a),type(a),len(a))
print("==========delete=======")
# del a[0] # By index
# a.remove("Test")#By value
# m=a.pop() # delete the last value from the list and return the deleted value 
m=a.pop(4)
print("Deleted value:-",m)
print(a)
print(id(a),type(a),len(a))