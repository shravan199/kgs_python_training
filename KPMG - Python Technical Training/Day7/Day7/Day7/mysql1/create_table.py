import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="Utkarsh_16_08"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS nishant_28 (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255),
address VARCHAR(255),
salary real)"""
)
#If the table already exists, use the ALTER TABLE keyword:
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
print('===========table created========')

mycursor = mydb.cursor()
#  
mycursor.execute("SHOW TABLES")
#  
for x in mycursor:
  print(x)