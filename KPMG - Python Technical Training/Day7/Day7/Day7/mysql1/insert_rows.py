import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="Utkarsh_16_08"
)

mycursor = mydb.cursor()

sql = "INSERT INTO nishant_28 (name, address) VALUES (%s, %s)"
val = ("Raju12", "Highway12 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")