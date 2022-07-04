import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading from CSV File
dataframe = pd.read_csv('scottish_hills.csv')
#print(dataframe)
#print(dataframe.head())

#print(dataframe.tail(3))
#print(dataframe['Hill Name'])
#print(dataframe['Height'])
#Gives you the row at position Five.
#print(dataframe.iloc[5])
#print(dataframe.iloc[0,3])
#getting all records with specified column
#print(dataframe.loc[:, ['Hill Name','Height', 'Latitude']])

#getting all columns with 1 and 10  records
print(dataframe.loc[[1,10], :])
print((dataframe.loc[(dataframe['Height']>500) & (dataframe['Hill Name']=='An Socach')]))

dd = (dataframe.loc[(dataframe['Height']>100) & (dataframe['Hill Name']=='An Socach')])
dds=dd.sort_values(by=['Height'], ascending=True)
print(dds.loc[:, ['Hill Name','Height', 'Latitude']])
#for scatter chart
x = dataframe.Height
y = dataframe.Latitude
plt.scatter(x, y)
plt.show()