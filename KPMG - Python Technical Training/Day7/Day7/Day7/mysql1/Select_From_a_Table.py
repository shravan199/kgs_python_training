import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="Utkarsh_16_08"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM nishant_28")
#mycursor.execute("SELECT * FROM customers LIMIT 5")

#mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
#myresult = mycursor.fetchone()

for x in myresult:
  print(x)
