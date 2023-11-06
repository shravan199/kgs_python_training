import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 34534", "Valley 345")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")