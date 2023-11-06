# a="NISHANT"
# print(a)
# 
# #b=a[0:7:2]#0,2,4,6>NSAT
# b=a[::4]# 0:len(a):4 > 0:7:4 > 0,4> NA
# print(b,type(b),len(b))
a=(10,10.8,"Nishant",(89,("Hii",)),90.78,"Test")
print(a)

b=a[::4]# 0:len(a):4 > 0:6:4 > 0,4> (10,90.78)
print(b,type(b),len(b))