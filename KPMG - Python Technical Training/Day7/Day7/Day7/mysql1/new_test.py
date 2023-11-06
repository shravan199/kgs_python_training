import pymysql
import pandas as pd 

connection = pymysql.connect("localhost","nishant","1234","mydatabase" )
cur=connection.cursor()
# cur.execute("SHOW TABLES")
# for i in cur:
#     print(i)
sql ='''CREATE TABLE if not exists weather_data(
   day VARCHAR(255) ,
   temperature VARCHAR(255),
   windspeed VARCHAR(255),
   event VARCHAR(255)
)'''
# cur.execute(sql)
cur.execute("CREATE TABLE IF NOT EXISTS weather_data (id INT AUTO_INCREMENT PRIMARY KEY,\
day VARCHAR(255),\
temperature VARCHAR(255),windspeed VARCHAR(255),\
   event VARCHAR(255))")
connection.commit()
cur.execute("SHOW TABLES")
#Closing the connection
for i in cur:
    print(i)

connection.close()