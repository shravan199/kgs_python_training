import json
obj=open('data.json','r')
# >json> python dict
dictObject=json.load(obj)
print(dictObject)
print(type(dictObject),len(dictObject))
print(dictObject['students'])
#####################################
#dict> json
json_data=json.dumps(dictObject)
print(json_data)
print(type(json_data),len(json_data))

#create/write  a json_data.json file ?













# for line in infile:
#     if line.strip().endswith('.mp3'):
#         print(line.strip(),file=outfile)
#     print(".")
# 
# outfile.close()
# infile.close()    
# if os.path.exists("out.txt") :
#     if os.path.getsize("out.txt")>0:  
#         print("file ready")
# print(os.path.getsize("out.txt")) #bytes
#     
# #check file have some data or not ?
# #write only the line that have hello.?
