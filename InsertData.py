# Python3 program to demonstrate SQLite3 datatypes
# and corresponding Python3 types

# import the sqlite3 package
import sqlite3

# create connection to database
cnt = sqlite3.connect('sql.db')
cursor = cnt.cursor()
query = "INSERT INTO users VALUES(4,'admin4','admin4', 'dharmarajpoudel@gmail.com','9851163785', 'admin', 1, '2022-06-13', '2022-06-13')"
cursor.execute(query)

cnt.commit()
print("Records created successfully")

# Insert tuples for the relation
cursor.execute("SELECT * from users ")
# display all data from users table
for row in cursor:
    print(row)


