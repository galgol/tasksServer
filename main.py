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

def add_to_available_tasks(client_input):
    mycursor, mydb = create_con_to_db()
    # creating a table called 'list_of_tasks' in the 'dbtest' database (if not exist)
    #from which the list of available tasks is saved, if needs to add new one add to here
    #this is a helper table (to create unique tasks at DB)
    mycursor.execute("CREATE TABLE IF NOT EXISTS list_of_tasks (task INT NOT NULL AUTO_INCREMENT,taskName VARCHAR(255) ,  PRIMARY KEY(task) ) ")
    query = "INSERT INTO list_of_tasks (taskName) VALUES ((%s))"
    client_input = client_input.decode()
    mycursor.execute(query, (client_input[2:],))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close()

def read_available_tasks(client_input):
    mycursor, mydb = create_con_to_db()
    # reading all records in table called 'list_of_tasks' in the 'dbtest' database
    #this is a helper table (to create unique tasks at DB)
    mycursor.execute("SELECT * FROM list_of_tasks ")
    result_table = mycursor.fetchall()  # fetch all records in db in order to print them
    for x in result_table:
        print(''.join((''.join(x[1])).split('2')),', with ID: ',x[0])
    mydb.close()

def insert_db(client_input):
    mycursor,mydb = create_con_to_db()
    # creating a table called 'tasks' in the 'dbtest' database (if not exist)
    #this is the table of tasks to do (main table) #date_task TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
    mycursor.execute("CREATE TABLE IF NOT EXISTS tasks (idTask INT NOT NULL AUTO_INCREMENT, task INTEGER,date_task TIMESTAMP DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY(idTask) , FOREIGN KEY(task) REFERENCES list_of_tasks(task)) ")
    query ="SELECT task FROM list_of_tasks WHERE task = %s"
    client_input = client_input.decode()
    client_input = int(client_input[2:]) #val is the values from client - the task to insert
    mycursor.execute(query, (client_input,))
    for row in mycursor.fetchall():
        task = row
        qry = "INSERT INTO tasks(task) VALUES ((%s))"
        mycursor.execute(qry, task)
        mydb.commit()#transaction to commit action to db
    print(mycursor.rowcount, "record inserted.")
    mydb.close()


def delete_from_db(client_input):
    mycursor, mydb = create_con_to_db()
    query =  "DELETE FROM tasks WHERE idTask = %s"
    client_input = client_input.decode()
    client_input =  (client_input[2:],) #val is the values from client - the task to delete
    mycursor.execute(query,client_input)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")
    mydb.close()

def print_all_table():
    mycursor, mydb = create_con_to_db()
    mycursor.execute("SELECT * FROM tasks")
    result_table = mycursor.fetchall() #fetch all records in db in order to print them
    for row in result_table:
        task = row[1]
        qry = "SELECT task, taskName FROM list_of_tasks WHERE task = %s"
        mycursor.execute(qry, (task,))
        result_val = mycursor.fetchall()
        print(row[0] ,result_val[0][1], row[2] )
    mydb.close()

def update_record_table(client_input):
    mycursor, mydb = create_con_to_db()
    query = "UPDATE list_of_tasks SET taskName = %s WHERE task = %s"
    client_input = client_input.decode()
    idx = client_input.find("#")  # '#' is the marker used to distingwish from old task to new
    client_input = (client_input[idx + 1:], int(client_input[idx-1])) #old value is second to send, inserted new value is first send
    mycursor.execute(query,client_input)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    mydb.close()

def close_all():
    print("bye bye ")