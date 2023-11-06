from ex1_connect import *
import time
conn,cur=connect()

sql="select * from kpmgAug23"
cur.execute(sql)
print("=======================Rows before Delete===================")
for i in enumerate(cur):#(indexNumber,row(tuple))
    print(f"{i[0]+1}",i[1])
print("========rows Deleting==============")
# sql="delete from kpmgAug23  where id=%s"
# row=(120,)
sql="delete from kpmgAug23  where name=%s and age=%s"
row=('Reena', 78)
cur.execute(sql,row)
conn.commit()
print("==========rows Deleted=====================")    
    
time.sleep(3)
sql="select * from kpmgAug23"
cur.execute(sql)
print("=======================Rows after Delete===================")
time.sleep(2)
for i in enumerate(cur):#(indexNumber,row(tuple))
    print(f"{i[0]+1}",i[1])
    
    
    
conn.close()