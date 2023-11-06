import os
infile=open("lines.txt",'r')#web ,python ,database
outfile=open('out.txt','w')

for line in infile:
    if line.strip().endswith('.mp3'):
        print(line.strip(),file=outfile)
    print(".")

outfile.close()
infile.close()    
if os.path.exists("out.txt") :
    if os.path.getsize("out.txt")>0:  
        print("file ready")
print(os.path.getsize("out.txt")) #bytes
    
#check file have some data or not ?
#write only the line that have hello.?
