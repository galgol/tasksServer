import mysql.connector

def create_db():
    mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "1"
      #database = "mydatabase"
    )
    # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
    mycursor = mydb.cursor()
    #creating a databse called 'dbtest'
    #'execute()' method is used to compile a 'SQL' statement
    #below statement is used to create tha 'dbtest' database
    mycursor.execute("CREATE DATABASE dbtest")

    #return mydb

def insert_db(val):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1",
        database = "dbtest"
    )
    mycursor = mydb.cursor()
    # creating a table called 'users' in the 'datacamp' database
    mycursor.execute("CREATE TABLE tasks (task VARCHAR(255) )")
    sql = "INSERT INTO tasks (task) VALUES (%s)"
    #val = val.decode('utf-8')
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")