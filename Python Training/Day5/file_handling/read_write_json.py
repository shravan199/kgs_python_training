import os
import json

os.chdir(r'D:\Python\Python Training\Day5\file_handling')
json_data = open('data.json', 'r')
# print(json_data.readlines())

# json => python dict obj
dict_obj = json.load(json_data)
# print(dict_obj)
# print(type(dict_obj), len(dict_obj))

# for k,v in dict_obj.items():
#     print(f'key: {k} and value: {v}')


# dict obj => json
json_data2 = json.dumps(dict_obj)
print(json_data2)
print(type(json_data2), len(json_data2))