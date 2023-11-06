# a=[]
# a=["Test"]
a=["Test",1,1.2,(1,2),[89,67],56.6]
print(a)
print(id(a),type(a),len(a))
b=a[2]#1.2 Indexing
b=a[2::2]#2:6:2> 2,4 >[1.2,[89,67]] #slicing
print(b)
#iterObject 
for i in a:
    print(i)