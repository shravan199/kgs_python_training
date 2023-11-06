_file = r'D:\Python\file_handling\file1.txt'

with open(file=_file, mode='r') as fo:
    print(f'File Object: {fo}')

    # for line in fo:
    #     print(line.strip())

    for line in fo.readlines():
        print(line.strip())

    print('Ending first for loop')

    fo.seek(0)
    for line in fo:
        print(line.strip())