import re
with open('lines.txt') as file :
    new=open('valid.txt','w')
    new1=open('invalid.txt','w')
    
    valid_no_list=[]
    invaild_no_list=[]
    m=0
    for line in file:
        m+=1
        out=re.findall(r'^[\w.%+-]{1,20}@[A-Za-z0-9.-]{2,20}[.][a-zA-Z]{2,3}$',line.strip())
        if len(out)!=0:
            valid_no_list.extend(out)
            new.write(out[0]+'\n')
        else:
            invaild_no_list.extend([line])
            new1.write(line)
            
print("Total Raw Emails:-",m)
print("total valid list number:- ",len(valid_no_list))
print("total invalid list number:- ",len(invaild_no_list))              
print("done")
        