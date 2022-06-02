# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)
file.close()
# reading content from different location
file2 = open(r"D:\reading\help.txt", "r")
#reads five character only
print (file2.read(5))
#read all the files content
print (file2.read())
file2.close()

# Python code to create a file and override
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

# Python code to illustrate split() function
with open("geek.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)



