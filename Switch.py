def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")

argument = 1
print (SwitchExample(argument))

#Looping Concept
x=0
#define a while loop
while(x <10):
    print(x)
    if x==3:
        break
    x = x + 1

x=0
while(x <10):
    x = x + 1
    if x==3:
        continue
    print(x)

#for with else
for y in range(6):
    if y ==3: break
    print(y)
else:
    print("Finished")

adj = ["red" ,"big" , "tasty"]
fruits = ["Apple" , "banana" , "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
#2D Array
#2D array with 4 rows and 5 columns
array=[
    [23,45,43,23,45],
    [45,67,54,32,45],
    [89,90,87,65,44],
    [23,45,67,32,10]
    ]
print(len(array))
#display
print(array)
#print first row
print(array[0])
#print second row 2 column
print(array[1][1])
for rows in array:
    for columns in rows:
        print(columns, end=" ")
    print()

rows, cols = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

rows, cols = (5,5)
arr=[]
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)
