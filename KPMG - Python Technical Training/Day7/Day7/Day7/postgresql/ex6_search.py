from ex1_connect import *
conn,cur=connect()

# sql="select * from kpmgAug23 where id=%s"
# row=(110,)#one value tuple
sql="select * from kpmgAug23 where name=%s and age=%s"
row=('Nishant',78)#one value tuple

cur.execute(sql,row)

# for i in enumerate(cur):#(indexNumber,row(tuple))
#     print(f"{i[0]+1}",i[1])

row_=cur.fetchall()
print(row_)