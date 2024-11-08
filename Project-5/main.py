""" Files Manager """


# os module works with file paths
import os 

# used for copying and moving files
import shutil

# Taking input by user to enter the path
path = input("Enter your path: ")

# Retrieves a list of all files and directories within the specified path
files = os.listdir(path)


# this loop will go through each file or directory found in that specified path
for i in files:
    
    #splits file name and its extension
    filename, extension = os.path.splitext(i)
    # Removes (.) from extension using slicing
    extension_1 = extension[1:]
    # constructs a path for folder named after the file extension
    folder_path = path + "\\" +extension_1


#check if folder already exists for the file's extension, if doesn't exist it will make by the name of extension and moves file in it.
    
    if os.path.exists(folder_path):
        shutil.move(path + "\\" + i, path + "\\" + extension_1 + "\\" +i)

    else:
        os.makedirs(folder_path)
        shutil.move(path + "\\" + i, path + "\\" + extension_1 + "\\" + i)




