# Create, write, and read file

f = open("demofile2.txt", "a")  # a: append, if file does not exist it creates the file
                                # w: overwrie, if file does not exist it creates the file
                                # "rt" - read Text - Default value. Text mode
                                # "rb" - read Binary - Binary mode (e.g. images)
                                # "wb" - write Binary - Binary mode (e.g. images)
                                
                                
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())


# Create a New File using open(filename, "x/a/w")
    # "x" - Create  will create a file, returns an error if the file exist
    # "a" - Append  will create a file if the specified file does not exist
    # "w" - Write   will create a file if the specified file does not exist
#f = open("myfile.txt", "x")


# To delete a file, you must import the OS module, and run its os.remove() function:
import os
#os.remove("demofile.txt")


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example: Check if file exists, then delete it:

# import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example Remove the folder "myfolder":
# Note: You can only remove empty folders.

# import os
#os.rmdir("myfolder")



# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:
#f = open("demofile.txt", "r")               # if in the same dir
print(f.read())

#f = open("D:\\myfiles\welcome.txt", "r")    # if in different dir
print(f.read())

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Example eturn the 5 first characters of the file:
#f = open("demofile.txt", "r")
print(f.read(5))


# Read Lines
# You can return one line by using the readline() method:
# Example Read one line of the file:
#f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())     # By calling readline() two times, you can read the two first lines:

# By looping through the lines of the file, you can read the whole file, line by line:
#Example Loop through the file line by line:
#f = open("demofile.txt", "r")
for x in f:
  print(x)


# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_file_remove.asp

#https://www.youtube.com/watch?v=2vmvtxHVPJI

#You can use a parameter in the with statement representing the file you're writing to. From there, use .write(). This assumes that everything in l is a string, otherwise you'd have to wrap all of them with str().
import array
l = ['3', '6', '9', '12', '60', '70']
#x/3.0
print(l)

with open('output', 'w') as f:
    f.write(l[1] + "\t" + l[2] + "\t" + l[3] + "\t" + l[4] + "\t" + l[5] + "\n")

#Alternatively, and more efficiently, you can use .join():

with open('output', 'w') as f:
    f.write('\t'.join(l[1:]) + '\n')
