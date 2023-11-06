import sqlite3 as sq 

conn=sq.connect("kpmg.db")
cur=conn.cursor()
rows=[(128,None,14,None,'Udai'),(129,None,23,"Nothing",'Geeta'),(120,45.90,29,"Rita BHag",'Vinesh'),
      (118,None,14,None,'Udai'),(119,None,23,"Nothing",'Geeta'),(111,45.90,29,"Rita BHag",'Vinesh')]

sql="insert into kpmgAug23 (id,salary,age,address,name) values (?,?,?,?,?)"
cur.executemany(sql,rows)#2nd Argument is a list of tuples  
conn.commit()
conn.close()