import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s and name=%s"
adr = ("Apple st 652",'Amy' )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")