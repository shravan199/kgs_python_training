import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
#Wildcard Characters=select the records that starts, includes, or ends with a given letter or phrase.
#sql = "SELECT * FROM customers WHERE address LIKE '%way%'"


#mycursor.execute(sql)

#SQL Injection
#
#sql = "SELECT * FROM customers WHERE address = %s"
#adr = ("Yellow Garden 2", )

#mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)