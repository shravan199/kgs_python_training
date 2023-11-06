from ex1_connect import *
import time
conn,cur=connect()

sql="select * from kpmgAug23"
cur.execute(sql)
print("=======================Rows before Update===================")
for i in enumerate(cur):#(indexNumber,row(tuple))
    print(f"{i[0]+1}",i[1])
print("========rows updating==============")
# sql="update kpmgAug23 set name=%s where name=%s"
# row=("Reena","Nishant")
sql="update kpmgAug23 set name=%s,address=%s where name=%s and age=%s"
row=("Jhon","Florida Home","Reena",25)
cur.execute(sql,row)
conn.commit()
print("==========rows updated=====================")    
    
time.sleep(3)
sql="select * from kpmgAug23"
cur.execute(sql)
print("=======================Rows after Update===================")
time.sleep(2)
for i in enumerate(cur):#(indexNumber,row(tuple))
    print(f"{i[0]+1}",i[1])
    
    
    
conn.close()