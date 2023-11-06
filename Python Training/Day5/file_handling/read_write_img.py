import os
os.chdir(r'D:\Python\Python Training\Day5\file_handling')

inImgName = 'pxl.jpeg'
inImg = open(inImgName, 'rb')
outImg = open('newPxl.jpeg', 'wb')

if os.path.exists(inImgName):
    in_img_bs = os.path.getsize('pxl.jpeg')
    print(f'Input image length: {in_img_bs} bytes')
    in_img = inImg.read(in_img_bs -20000)
    outImg.write(in_img)
else:
    print(f'image {inImgName} not found')


