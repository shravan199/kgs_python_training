from ex1_connect import *
conn,cur=connect()
#insert one row into table kpmgAug23
# row=(5,'Nishant',78,"New Data",45.6996)#We can't handle null values like that
# sql="insert into kpmgAug23 (id,name,age,address,salary) values " + str(row)
#cur.execute(sql)
#insert one row into table kpmgAug23 using sql injection.
# row=(6,'Nishant',78,None,None)
# sql="insert into kpmgAug23 (id,name,age,address,salary) values (%s,%s,%s,%s,%s)"
# cur.execute(sql,row)#2nd Argument is a tuple value 
#insert list of  rows(tuples) into table kpmgAug23 using sql injection.
# rows=[(17,'Nishant',78,None,None),(18,'Raj',98,None,None),(19,'Nishant',78,"Mawan meerut",478.979),
#       (110,'Raj',98,"Gol puri",765.90)]
#insert the given rows into the table 
rows=[(128,None,14,None,'Udai'),(129,None,23,"Nothing",'Geeta'),(120,45.90,29,"Rita BHag",'Vinesh'),
      (118,None,14,None,'Udai'),(119,None,23,"Nothing",'Geeta'),(111,45.90,29,"Rita BHag",'Vinesh')]

sql="insert into kpmgAug23 (id,salary,age,address,name) values (%s,%s,%s,%s,%s)"
cur.executemany(sql,rows)#2nd Argument is a list of tuples  
conn.commit()
conn.close()