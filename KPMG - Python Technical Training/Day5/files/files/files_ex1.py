#obj=open(filename,mode)# r>read,w>write,r+>read/write ,a>append
# obj=open("lines.txt",'r')
# print(obj)
# for line in obj:
#     print(line.strip())
# 
# obj.seek(0)
# f=obj.readlines()#list of lines#obj.readline()
# print(f)
# obj.close()
# 
# obj.readline()
with open("lines.txt") as obj:
    for line in obj:
        print(line.strip())
        
        
obj.readline()
        
        
    