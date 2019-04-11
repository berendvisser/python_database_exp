import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    passwd="password",
    database="pythontest"
    )

mycursor = mydb.cursor()


#mycursor.execute("SELECT * FROM tables")


#myresult = mycursor.fetchall()


    
mycursor.execute("UPDATE dmx SET `1.00` = '255' WHERE CHANNEL = 2")
mydb.commit()
print(mycursor.rowcount, "record inserted.")