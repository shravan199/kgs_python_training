import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Utkarsh_16_08")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)