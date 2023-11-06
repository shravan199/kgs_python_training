import re

# str="Sat hat mat paat #at_at.at 9at (at"
# out=re.findall('^[shmpa]at',str)
# print(out)

# str=['Sat hat mat +++ pat','Hatmatpat not bad ...',
#      'hatlo 90*&6 hii hmmmm','aat','@at234'] 
# print(str)
# # #if First 3 char matched return full string list? dnt use if -else ,update regex
# #'^[Shmpa]at' >> 
# #output: ['Sat hat mat +++ pat','hatlo 90*&6 hii hmmmm','aat']
# matched_list=[]
# for i in str:
#     out=re.findall('^[Shmpa]at.*',i)
#     matched_list.extend(out)
# 
# print(matched_list)
str=['+91-222-81345','+82-333-82456','+56-356-67894','+43-333-89456','+99-888-67897','+56-5678-67890', '+91-676-8905678','1+91-222-81345']
print(str)
matched_list=[]
for i in str:
    out=re.findall('^\+[985][1-6]-\d{3}-\d{5}$',i)
    matched_list.extend(out)

print(matched_list)






