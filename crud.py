import mysql.connector
# It’s a Python library used to connect Python with MySQL databases.

# connect to the database server
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'indigo'
    )

    mycursor = conn.cursor() # A cursor is like a pointer or controller that allows Python to execute SQL commands and interact with your database connection.
                             # Think of it as your “database worker” — you tell it what SQL to run, and it goes and does it for you.
    print("Connection Established")
except:
    print("Connection Error")

#creates a Database on db server by using python
#mycursor.execute("CREATE DATABASE indigo")
#conn.commit()

#creates a table
#mycursor.execute("""
#CREATE TABLE airport(
#    airport_id INTEGER PRIMARY KEY,
#    code VARCHAR(10) NOT NULL,
#    city VARCHAR(50) NOT NULL,
#    name VARCHAR(255) NOT NULL
#    )
#""")
#conn.commit()

#mycursor.execute("""
#INSERT INTO airport VALUES
#    (1,'DEL','New Dehli','IGIA'),
#    (2,'CCU','Kolkata','NSCA'),
#    (3,'BOM','Mumbai','CSMA')"""
#)
#conn.commit()

# Retrieve data from the table

#mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
#data = mycursor.fetchall()
#print(data)

#for i in data:
#    print(i[2])

# we can also do update,delete etc just like in mysqlworkbench
