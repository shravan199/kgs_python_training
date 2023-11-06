# obj=open(filename,mode)# r>read,w>write,r+>read/write ,a>append
import os
print(os.getcwd())
os.chdir(r'D:\Python\Python Training\Day5\file_handling')
print(os.getcwd())

fo = open(r"lines.txt")
print(fo)

for line in fo:
    print(line.strip())

fo.seek(0)
print(fo.readline())
fo.close()

x = fo.readline()
print(x)
