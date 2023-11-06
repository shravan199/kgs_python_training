obj=(1,1.2,"Nishant",(56,89),[89,90])

for i in obj:
    print(i,type(i))
    
for m in ["Nishant","Suresh","Shyam","Radha Rani","Krishna","Naresh"]:
    print(m)
    if m!="Naresh":
        print(m,"Please join my evening Party")
        
# print "hello" 1000 times ?
##############################
# for m in range(5):
#     print(m)
#     
# for m in range(3,10,3):
#     print(m)
k=0    
for i in range(1000):
    k += 1
    print(k,"Hello")