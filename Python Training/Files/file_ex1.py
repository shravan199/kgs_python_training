import os
print(os.getcwd())

os.chdir(r"D:\Python\Python Training\Files")

with open('lines.txt') as fo:
    print(fo)
    for line in fo:
        print(line.strip())
    
    fo.seek(0)
    print(fo.readlines())

