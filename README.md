# tasksServer
# tasksServer- this is my personal project using python and mysql
I wanted to learn the basics of DB and create a server-client app that involves DB actions,
while writing a local server on my computer with a DB. The server runs on my local computer and listens on a port.
The server has 2 endpoints:
1. endpoint  that saves data - I can write a task to insert to the db (from client and send to server)
2. endpoint that returns data - I can ask for the server to return to me all the tasks that are in the db.

# This project has 3 main files:
1. echoserver.py - is the server side of the app which has the connection creation with client
and all the data (requests) from client which is handled by request.
2. echoclient.py - is the client side of the app which has also the connection creation with server
and all the data (requests) that is inserted (from commandline) and then send to server.
3. main.py - is the db - creation of the db and tables and handle data with functions (which are called from server) according to users choice (client)

# In order to strat this app:
open first commandline: ./echoserver.py - here the server listens on port and handle all request with DB
open second commandline: ./echoclient.py - here there is a menu bar which we choose action to prefrom 
# If we want to check what happens on db itself: install mysql  (if you havent got it on your PC)
in a new commandline:
1. sudo systemctl start mysql #restart mysql
2./usr/bin/mysql -u root -p #opens mysql
3. SHOW DATABASES; #shows all db on mysql
4.use dbtest; #select the db which was used for the app
5.SHOW TABLES; #show all tables in db
6.SELECT * FROM tasks; # prints all records in table (all the records we inserted from app)

***i have created 2 tables :
1. list of tasks - which has all options for tasks (id,name)
2. tasks - all TODO tasks which is taken from table1 and has data of insertion (id,forigen id, date)