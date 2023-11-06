a=["Test",1,"Test",1.2,"Test",(1,2),"Test",[89,67],"Test","Test",56.6,"Test"]
print(a)
print(id(a),type(a),len(a))
print("==========delete=======")
#create a list of Value "Test" index numbers . ?
indices =[]
index= 0
for item in a:
    if type(item) == str and item.lower() == 'test':
        indices.append(index)
    index += 1

print(indices)
#[0,2,4....]
#Delete all the "Test" Values from given list ? 

for item in a:
    
    if type(item) == str and item.lower() == 'test':
        a.remove('Test')

print(a)