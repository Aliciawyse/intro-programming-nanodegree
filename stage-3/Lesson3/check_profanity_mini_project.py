# Lesson 3.3: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarassing! Imagine how youd feel if you
# accidentally sent your boss an email that said I'll take
# a sh?t at it, instead of Ill take a shot at it. Write
# a program that can detect curse words in a string of text.

import urllib

def read_text():
    #Open my local file that includes text I'd like to check for profanity.
    fhand = open('movie_quotes.txt')
    
    #Read the contents of my file.
    contents_of_my_local_file = fhand.read()
    
    #print contents_of_my_local_file
    
    #Close file.
    fhand.close()
    
    #call the check profanity function while passing in the contents of my file.
    check_profanity(contents_of_my_local_file)


def check_profanity(text_to_check):
    
    #Open a connection to the What Do You Like website. Construct the URL with the contents of our local file.
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=shot'+ text_to_check)
    
    #Read response from website
    output = connection.read()
    
    #print(output)
    connection.close()
    
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print ("This document has no curse words.")
    else: 
        print ("Could not scan document properly.")
    
read_text()


