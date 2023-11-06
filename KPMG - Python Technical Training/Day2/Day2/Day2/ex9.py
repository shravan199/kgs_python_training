#string methods 
name="Nishant"
surname="Sharma"
age=90
#dynamic string
out="Name:- "+name+" "+surname +" Age :- "+str(age)
print(out)
#format method 
#{} > placeholder
out="Name :- {} age :- {}".format(name,age)
print(out)
out="Name :- {1} age :- {0}".format(name,age) #Index Numbers:- name> 0  age > 1
print(out)
# len of {} <= len Variables passed into format method
#f-string method
out=f"Name :- {name} age :- {age}"
print(out)