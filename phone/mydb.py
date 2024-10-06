import mysql.connector
dataBase=mysql.connector.connect(
    host="Janany",
    user="root",
    password="Jan@12345"

)
cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE address")

print("All Done!")
