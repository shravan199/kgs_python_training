import sqlite3 as sq 

conn=sq.connect("kpmg.db")
cur=conn.cursor()
sql="""create table if not exists kpmgAug23(
id integer primary key not null,
name text not null,
age integer not null,
address char(50),
salary real)
"""

cur.execute(sql)


conn.commit()

conn.close()