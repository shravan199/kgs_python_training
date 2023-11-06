a=[1,5,3,4,2,7,8,10,9,6]
print(a)
print(id(a),type(a),len(a))
#a.reverse()
# a.sort()
a.sort(reverse=True)
print(a)
print(id(a),type(a),len(a))
#####################list&tuple+++++++++++
from numpy import mean
m=mean(a)#len(a)#max(a)#min(a)#sum(a)
print(m)