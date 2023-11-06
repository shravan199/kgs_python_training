a="NISHANT"
a=(10,10.8,"Nishant",(89,("Hii",)),90.78,"Test")
print(a)

b=a[-2] #90.78
print("The value is b :-",b)

# get the index number of Value Hii from given tuple a ?
b=a[3][-1][0]
print(b)
# Try to update  the value of tuple object
#a[2]="Manish"
#TypeError: 'tuple' object does not support item assignment
#del a[2]
#TypeError: 'tuple' object doesn't support item deletion