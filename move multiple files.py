# Python 101-02 - Example 1
# Move multiple files to Multiple folder and renames them
# It takes the name of a pdf file and create a folder base on that name and then move the pdf file to the new folder and then rename the file to ad,pdf

import os

for filename in os.listdir(r"C:\Users\Muhammad\Desktop\New Jobs Copy"): # Pay attention to the ending : for a for loop
    if filename.endswith('.pdf'):   
        print(filename)
        
# This is the way we chech for pdf files Otherwise folders and other extenstions would show up. 
# Also pay attention to the ending : for an if statement

# This was a simple test. Now lets create folder for each pdf file using the same name of pdf file
rootFolder = r"C:\Users\Muhammad\Desktop\New Jobs Copy"

for filename in os.listdir(rootFolder): # Pay attention to the ending : for a for loop
    if filename.endswith('.pdf'):   
        newFolderPath = rootFolder + '\\' + os.path.splitext(filename)[0] # We simply remove the file extension to get the path of the new folder! [1] is the .extension
        
        print(newFolderPath)

        if not os.path.exists(newFolderPath):
            os.mkdir(newFolderPath)

        os.rename(rootFolder + '\\' + filename, newFolderPath + '\\ad.pdf')
# End!