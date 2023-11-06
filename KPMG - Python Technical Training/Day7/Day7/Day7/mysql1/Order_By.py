import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="mydatabase"
)

mycursor = mydb.cursor()
#The ORDER BY keyword sorts the result ascending by default.

sql = "SELECT * FROM customers ORDER BY name"
#To sort the result in descending order, use the DESC keyword.
#sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)