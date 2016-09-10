#Your friend has hidden your keys. To find out where they are, 
#you have to remove all numbers from the files in the folder
#called prank. 

import os # the os, operating system, module allows you to access files and directories 

def rename_files():
    #get the file names
    file_list = os.listdir(r"/home/ubuntu/workspace/stage3/Lesson1/rename_exercise")
    
    #saved_path = os.getcwd()
    #print saved_path
    
    #Our program wasn't in the correct directory, so we use this method to 
    #change the current working directory
    os.chdir(r"/home/ubuntu/workspace/stage3/Lesson1/rename_exercise")

    #for each file name, rename it by removing numbers
    for file in file_list:
        os.rename(file, file.translate(None,"0123456789"))
    
    print file_list    
    
rename_files()

#if you try to rename a file that doesnt exist or try to use a name that already exists, you'll get an exception error. 