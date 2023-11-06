import os, time
print(os.getcwd())
print(os.listdir())
os.chdir(r"D:\Python\Python Training\File Handling")
print(os.getcwd())
print(os.listdir())
#os.mkdir('newfolder2/sys')
print(os.getcwd())

if not os.path.exists('newfolder2/sys1'):
    os.mkdir('newfolder2/sys1')

time.sleep(2)

with open('newfile.txt', 'w') as file:
    file.write('new file created')

print(os.listdir())

print('walk function')
dirs = os.walk(r"D:\Python\Python Training\File Handling")
print(dirs)

for path, folder, files in dirs:
    print(path, folder, files)
