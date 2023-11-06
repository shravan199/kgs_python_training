import os
infile=open("lines.txt",'r')#web ,python ,database
outfile=open('out.txt','a')

for line in infile:
    print(line.strip(),file=outfile)
    print(".")
    
if os.path.exists("out.txt") :
    if os.path.getsize("out.txt")>=os.path.getsize("lines.txt"):  
        print("file ready")
print(os.path.getsize("lines.txt")) #bytes
    
#check file have some data or not ?
#write only the line that have .mp3.?
