import os

os.chdir(r"D:\Python\Python Training\Files")

with open('lines.txt') as ifo:
    pass

with open('out.txt', 'a') as ofo:
    ofo.write('new line')
