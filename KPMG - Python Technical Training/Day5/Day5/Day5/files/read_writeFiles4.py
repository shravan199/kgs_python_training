import os
infile=open("bigfile.txt",'rb')#web ,python ,database
outfile=open('out.txt','wb')
buffer_size=31 #bytes
buffer=infile.read(buffer_size)

while buffer:
    outfile.write(buffer)
    buffer=infile.read(buffer_size)
    print(".")

outfile.close()
infile.close()    
if os.path.exists("out.txt") :
    if os.path.getsize("out.txt")>0:  
        print("file ready")
print(os.path.getsize("out.txt")) #bytes






















# for line in infile:
#     if line.strip().endswith('.mp3'):
#         print(line.strip(),file=outfile)
#     print(".")
# 
# outfile.close()
# infile.close()    
# if os.path.exists("out.txt") :
#     if os.path.getsize("out.txt")>0:  
#         print("file ready")
# print(os.path.getsize("out.txt")) #bytes
#     
# #check file have some data or not ?
# #write only the line that have hello.?
