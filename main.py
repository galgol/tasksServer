import mysql.connector

def create_db():
    mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "1"
    )
    # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
    mycursor = mydb.cursor()
    #creating a databse called 'dbtest'
    #'execute()' method is used to compile a 'SQL' statement
    #below statement is used to create the 'dbtest' database
    mycursor.execute("CREATE DATABASE IF NOT EXISTS dbtest")
    mydb.close() #close current connection

def create_con_to_db(): #function to create a connection to this db (dbtest)
    mydb = mysql.connector.connect(
        host="localhost",
            user="root",
            password="1",
            database = "dbtest"
        )
    return mydb.cursor() , mydb

def insert_db(val):
    mycursor,mydb = create_con_to_db()
    # creating a table called 'tasks' in the 'dbtest' database (if not exist)
    mycursor.execute("CREATE TABLE IF NOT EXISTS tasks (task VARCHAR(255) )")
    query = "INSERT INTO tasks (task) VALUES ((%s))"
    val = val.decode()
    val = val[2:] #val is the values from client - the task to insert
    mycursor.execute(query, (val,))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close()


def delete_from_db(val):
    mycursor, mydb = create_con_to_db()
    query =  "DELETE FROM tasks WHERE task = %s"
    val = val.decode()
    val =  (val[2:],) #val is the values from client - the task to delete
    mycursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")
    mydb.close()

def print_all_table():
    mycursor, mydb = create_con_to_db()
    mycursor.execute("SELECT * FROM tasks")
    result_table = mycursor.fetchall() #fetch all records in db in order to print them
    for x in result_table:
        print(''.join(x))
    mydb.close()

def update_record_table(val):
    mycursor, mydb = create_con_to_db()
    query = "UPDATE tasks SET task = %s WHERE task = %s"
    val = val.decode()
    idx = val.find("#") # '#' is the marker used to distigwish from old task to new
    val =  (val[idx+1:] , val[2:idx]) #old is first, new is second
    mycursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    mydb.close()

def close_all():
    print("bye bye ")