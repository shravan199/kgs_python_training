# obj=open(filename,mode)# r>read,w>write,r+>read/write ,a>append
import os
print(os.getcwd())
os.chdir(r'D:\Python\Python Training\Day5\file_handling')
print(os.getcwd())

with open(r'lines.txt') as fo:
    for line in fo:
        print(line.strip())

    fo.seek(0)
    print(fo.readline())
    print(fo.readlines())
