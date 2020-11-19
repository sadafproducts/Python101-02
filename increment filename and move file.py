# Python 101-02 - Example 2
# Move multiple files by incrementing filename and move them to new folders

import os

rootFolder = r"C:\Users\Muhammad\Desktop\New Jobs 2"

for filename in os.listdir(rootFolder):
    if filename.endswith('.pdf'):
        newFolderName = os.path.splitext(filename)[0]
        newFolderPath = rootFolder + '\\' + str(int(newFolderName)+43) # To increment filename you need to convert string to int and int to string 
        #print(newFolderPath)        
        
        if not os.path.exists(newFolderPath):
            os.mkdir(newFolderPath)

        os.rename(rootFolder + '\\' + filename, newFolderPath + '\\1 ad.pdf')
