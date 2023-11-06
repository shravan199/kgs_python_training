# seq=[78,89,34,35,36,67,89]
# g=list(filter(lambda x : x%2!=0,seq))
# print(g)
input="I43N4D4I43@4123D34E3L44H5I"
h="".join(list(filter(lambda x : not x.isdigit() ,input)))
print(h)

#create a list of 1000 numbers ?
# out=[]
# for i in range(1,1001):
#     out.append(i)
# print(out)
# list comprehension in python
# [value for loop_var in iterObject]
g=[i for i in range(1,1001)]
print(g)
# [value for loop_var in iterObject if exp]
g=[i for i in range(1,20) if i%2==0]
print(g)

# [value1 if exp else value2 for loop_var in iterObject ]
g=[i if i%2==0 else "Odd" for i in range(1,20) ]
print(g)
