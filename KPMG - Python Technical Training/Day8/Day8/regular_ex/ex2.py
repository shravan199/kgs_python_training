import re
str='we need to inform him with the latest information'
#The expression re.findall() returns all the non-overlapping
#matches of patterns in a string as a list of strings. 
allinform=re.findall('inform ', str)
print(allinform)
for i in allinform:
    print(i)