import os, shutil

print(os.getcwd())

print(os.listdir())

# for dir, dirs, filenem in os.walk(os.getcwd()):
#     print(dir)
#     print(dirs)
#     print(filenem)
#     print()

os.chdir(os.getcwd()+'\Day5\os_operations')
print(os.getcwd())

#os.mkdir(r'newFolder0\test')
print(os.getcwd())

#os.rename('newFolder2', 'newFolder2_old')
if os.path.exists(path=r'newFolder2\test3.txt'):
    pass
else:
    os.makedirs(r'newFolder2\test3.txt')

import time
time.sleep(2)

if os.path.exists(r'newFolder2\sys'):
    # os.removedirs(r"newFolder2\sys") #remove only sub dir
    shutil.rmtree('newFolder2\sys', ignore_errors=False)
else:
    print(f'path \'newFolder2\\test3.txt\' doest not exist')
    

print(f'List of directories: {os.listdir( )}')


g= os.walk(r'D:\Python\Python Training\Day4')

for paths, folders, files in g:
    if 'bounce.py' in files:
        print(paths)
path = 'newFolder2\sys'
print(f"""is file :{os.path.isfile(path)}""")

shutil.copy()