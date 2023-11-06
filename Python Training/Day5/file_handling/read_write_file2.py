import os
os.chdir(r'D:\Python\Python Training\Day5\file_handling')

inFile = open('lines.txt', 'r')
outFile = open('out.txt', 'r+')
buffer_size= 89
inFileData  = inFile.read(buffer_size)
print(inFileData)

out_bs = outFile.write(inFileData)
print(out_bs)