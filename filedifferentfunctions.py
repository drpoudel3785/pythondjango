import os
import shutil
if not os.path.isdir("helpme"):
    os.mkdir("helpme")
path = os.chdir("D:\CLASS\Training\PYTHONDJANGO\CODES\helpme")
print(path)
file2 = open(r"D:\reading\help.txt", "r")
# Python code to create a file and override
file = open('helpme.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
#os.remove("helpme.txt")
#os.rmdir("admin123")
path = os.chdir("D:\CLASS\Training\PYTHONDJANGO\CODES")
#os.rmdir('helpme')
shutil.rmtree('helpme')
# getting the current directory info
print(os.getcwd())
# Change the current directory
#os.chdir('D:\\CLASS')
#print(os.getcwd())



#renaming the dharma.txt to poudel.txt
if os.path.exists('dharma.txt'):
    os.rename('dharma.txt' , 'poudel.txt')

#delete the file
if os.path.exists('poudel.txt'):
    os.remove('poudel.txt')


path="admin123"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
    print(path, " directory created")
else:
    print(path, "admin directory already exists")

print(os.listdir("admin"))
for x in os.listdir("admin"):
    print(x)

for x in os.listdir("D:\CLASS\Training\PYTHONDJANGO\CODES"):
    if os.path.isfile(x): print('File - ', x)
    elif os.path.isdir(x): print("Directory - ", x)
    else: print("-----", x)


# Program to show various ways to
# read and write data.



# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()
# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)
print("Output of Readline function is ")
print(file1.readline())
print()
file1.seek(0)
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
