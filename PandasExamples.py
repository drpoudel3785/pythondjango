import pandas as pd
import numpy as np


#reading from CSV File
df = pd.read_csv('phonenumbers.csv')
print(df.to_string())

pd.options.display.max_rows = 3
df = pd.read_csv('phonenumbers.csv')

print(df.to_string())


#Reading json
df = pd.read_json('sample2.json')
print(df.to_string())


#Pandas Series is a one-dimensional labeled array capable of holding
# data of any type (integer, string, float, python objects, etc.)

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data, index=[10,11,12,13,14])

#ser = pd.Series(data)
print(ser)

#creatring a series from list
list = ['P','Y','T','H','O','N','T','R','A','I','N','I','N','G']
ser = pd.Series(list)
print(ser)

#creating a series form Dictionery
dict = {
    'Python' : 20000,
    'Java': 30000,
    'C#': 50000
}
ser = pd.Series(dict)
print(ser)

#Pandas DataFrame
# is a two dimensional tabular data structure
# data is aligned in a tabular fashion in rows and columns
# Pandas DataFrame consists of three principal components , the data, the rows and columns
df = pd.DataFrame()
print(df)

list = ['P','Y','T','H','O','N','T','R','A','I','N','I','N','G']
df = pd.DataFrame(list)
print(df)


data =[['Ram', 40],['Sita', 39], ['Manish', 10]]
df= pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

salary =[['Ram', 40000],['Sita', 50000], ['Manish', 1000000]]
df= pd.DataFrame(data, columns=['Name', 'Salary'] )
print(df)

#creating DataFrame via dictionery
data = {'Name':['Ram', 'Sita', 'Manish'], 'Age':['40', '39', '20'], 'Salary':[40000, 50000, 100000]}
df=pd.DataFrame(data)
print(df)


