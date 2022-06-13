# Python3 program to demonstrate SQLite3 datatypes
# and corresponding Python3 types

# import the sqlite3 package
import sqlite3

# create connection to database
cnt = sqlite3.connect('sql.db')

# Create a users relation
cnt.execute('''CREATE TABLE users(
id INTEGER,
username TEXT,
password TEXT,
email TEXT,
phone TEXT,
usertype TEXT,
status INTEGER,
createddate TEXT,
updateddate TEXT
);''')

cnt.close()