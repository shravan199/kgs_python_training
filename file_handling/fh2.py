in_file = r'D:\Python\file_handling\file1.txt'
out_file = r'D:\Python\file_handling\out.txt'

try : 
    info = open(file=in_file, mode='r')
    outfo = open(file=out_file, mode='a')
    
    for line in info.readlines():
        print(line.strip(), file=outfo)
    
    print(f'Content copied successfully.')

except Exception as e:
    print(f'Error: {e}')
finally:
    try: 
        info.close()
        outfo.close()
    except:
        pass