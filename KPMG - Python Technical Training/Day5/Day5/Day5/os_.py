import os,time,shutil
print(os.getcwd())
print(os.listdir()) 
os.chdir(r"C:\Users\OM\eclipse-workspace\KpmgAug2023\Day4")
print(os.getcwd())
print(os.listdir())
#os.mkdir("newfolder/sys")
# os.rename("newfolder2","test")
# if os.path.exists("newfolder2/sys"):
#     pass
# else:
#     os.makedirs("newfolder2/sys")
#os.rmdir("test/sys")#remove only sub dir
# os.removedirs("test/sys")
# shutil.rmtree("test/sys",ignore_errors=True)#delete the dir with/without content
# time.sleep(2)
# print(os.listdir())

g=os.walk(r"C:\Users\OM\eclipse-workspace\KPMG17Jan_01Feb22")
print(g)
for path,folders,files in g:
    print("path:-",path)
    print("List of folders:-",folders)
    print("List of files:-",files)
    print()
    if "lines.txt" in files:
        print(path)

print(os.path.isfile("hello"))
print(os.path.isdir("test"))











