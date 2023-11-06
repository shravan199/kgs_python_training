# check file have some data or not ?
# write only the line that have hello.?
import os
print(os.getcwd())
os.chdir(r'D:\Python\Python Training\Day5\file_handling')
print(os.getcwd()) 
print()

file_obj = open(file='lines.txt', mode='r')
of = open('out.txt', mode='a+')

print(f"length of file: {len(file_obj.readlines())}")

if len(file_obj.readlines()) == 0:
    print(f'file is empty')
else:
    print(file_obj.readlines())

fileName = 'lines.txt'
print(f'Size of file: {os.path.getsize(fileName)}')
if os.path.getsize('lines.txt') > 0:
    print(f'file has some data')
else:
    print(f'file is empty')

file_obj.seek(0)
if os.path.exists(fileName):
    for line in file_obj.readlines():
        if 'mp3' in line.strip():
            print(line.strip(), file=of)
            print(f' line: {line} is writen in output file')
else:
    print(f'File doesn\'t exist')

of.seek(0)
for line in of:
    print(line.strip())