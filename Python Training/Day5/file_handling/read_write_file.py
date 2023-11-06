import os
print(os.getcwd())
os.chdir(r'D:\Python\Python Training\Day5\file_handling')
print(os.getcwd())

inFile = open('lines.txt', 'r')
outFile = open('out.txt', 'a')

for line in inFile:
    print(line.strip(), file=outFile)
    print('.')

if os.path.exists('out.txt'):
    print(f'file ready')