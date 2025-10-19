import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
    )
    mycursor = mydb.cursor()
    if mydb.is_connected():
        print("Connected to MySQL!")

        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database created successfully")
        mydb.commit()

except mysql.connector.Error as e:
    print("Failed to connect to MySQL!",e)

finally:
    mycursor.close()    
    mydb.close()
    print("MySQL connection is closed")
