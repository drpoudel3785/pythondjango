import sqlite3
# create connection to database
cnt = sqlite3.connect('sql.db')
print("Opened database successfully")
cursor = cnt.cursor()
cnt.execute("DELETE FROM users WHERE id = 3")
cnt.commit()
print ("Data Deleted :", cnt.total_changes)
cursor = cnt.execute("SELECT id, username, password, email, status FROM users")
for row in cursor:
   print ("ID = ", row[0])
   print ("USERNAME = ", row[1])
   print ("PASSWORD = ", row[2])
   print ("EMAIL = ", row[3])
   print("STATUS = ", row[4], "\n")
print ("Operation done successfully")
cnt.close()