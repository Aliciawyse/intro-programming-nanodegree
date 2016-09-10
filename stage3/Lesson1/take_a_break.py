#Write a program that prompts the user to take a break 
#once every two hours, a maximum of three times. 

import webbrowser #Displays web-based documents to users
import time #This module provides various time-related functions


total_breaks = 3
count = 0 

print "This program started on ", time.ctime() #time.ctime show local time. 

while count < total_breaks:
    time.sleep(7200)        #There are seventy-two hundred seconds in two hours   
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=RB9fVasnfXk')
    count = count + 1
