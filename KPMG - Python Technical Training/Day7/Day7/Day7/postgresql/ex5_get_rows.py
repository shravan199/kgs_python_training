from ex1_connect import *
conn,cur=connect()

# sql="select id,age,name from kpmgAug23"
sql="select * from kpmgAug23"

cur.execute(sql)

# for i in enumerate(cur):#(indexNumber,row(tuple))
#     print(f"{i[0]+1}",i[1])

# g=cur.fetchone()#return one row 
# g=cur.fetchmany()#return list of one row(tuple)
#g=cur.fetchmany(-1)#return list of all rows(tuples)
# g=cur.fetchmany(4)#return list of 4 rows(tuples)
g=cur.fetchall()#return list of all rows(tuples)
print(g)
print(len(g))
import pandas as pd 
df=pd.DataFrame(data=g,columns=['id','name','Age',"Address","Salary"])
print(df.info())
print(df)
df.to_excel("New.xlsx",sheet_name="nishant_data",index=False)
conn.close()