from ex1_connect import *
conn,cur=connect()

sql="""create table if not exists kpmgAug23(
id int primary key not null,
name text not null,
age int not null,
address char(50),
salary real)
"""

cur.execute(sql)


conn.commit()
conn.close()