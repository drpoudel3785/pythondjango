import datetime
from datetime import date

#Get Current Date and Time
datetime_object = datetime.datetime.now()
print(datetime_object)

#Get Current Date
date_object = datetime.date.today()
print(date_object)

#We can use dir() function to get a list containing all attributes of a module.
print(dir(datetime))

# current date and time
now = datetime.datetime.now()
d = now.strftime("%Y %m %d")
print("Date:", d)

t = now.strftime("%H:%M:%S")
print("time:", t)
print(dir(date))






