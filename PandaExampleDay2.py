import pandas as pd
import numpy as np
#Create a series with random numbers
s = pd.Series(np.random.randn(4))
print ("Is the Object empty?")
print(s.empty)
#s = pd.Series()
#print(s.empty)
#Returns the number of dimensions of the object. By definition, a Series is a 1D data structure, so it returns
print(s)
print ("The dimensions of the object:")
print(s.ndim)


#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our data series is:")
print(df)
print(df.shape)
#transpose of the above series dictionary
print(df.T)
#Returns a tuple representing the dimensionality of the DataFrame. Tuple (a,b), where a represents the number of rows and b represents the number of columns.
print(df.shape)
#Returns the number of elements in the DataFrame.
print ("The total number of elements in our object is:")
print(df.size)

# Returns the actual data in the DataFrame as an NDarray.
print(df.values)

#To view a small sample of a DataFrame object, use the head() and tail() methods. head() returns the first n rows (observe the index values). The default number of elements to display is five, but you may pass a custom number.
print(df.head(2))
#tail() returns the last n rows (observe the index values). The default number of elements to display is five, but you may pass a custom number.
print(df.tail(3))

#Returns the sum of the values for the requested axis. By default, axis is index (axis=0).
print(df.sum())

print(df.sum(0))
#Returns the average value
print("Returns the average value")
print(df.mean())

#Returns the Bressel standard deviation of the numerical columns.
print("the Bressel standard deviation ")
print(df.std())

#Let us now understand the functions under Descriptive Statistics in Python Pandas. The following table list down the important functions −

##1	count()	Number of non-null observations
#2	sum()	Sum of values
#3	mean()	Mean of Values
#4	median()	Median of Values
#5	mode()	Mode of values
#6	std()	Standard Deviation of the Values
#7	min()	Minimum Value
#8	max()	Maximum Value
#9	abs()	Absolute Value
#10	prod()	Product of Values
#11	cumsum()	Cumulative Sum
#12	cumprod()	Cumulative Product

#The describe() function computes a summary of statistics pertaining to the DataFrame columns.
print(df.describe())

#akes the list of values; by default, 'number'.

#object − Summarizes String columns
#number − Summarizes Numeric columns
#all − Summarizes all columns together (Should not pass it as a list value)
print(df.describe(include=['object']))

print("the minimum value is: ")
print(df.min())
print("the Maximum value is: ")
print(df.max())

print(df.sort_index(ascending=False, axis=1))

print(df.sort_values(by='Name', ascending=True))