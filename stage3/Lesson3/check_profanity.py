# Lesson 3.3: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarassing! Imagine how youd feel if you
# accidentally sent your boss an email that said I'll take
# a sht at itninstead of Ill take a shot at it. Write
# a program that can detect curse words in a string of text.

import urllib

def read_text():
    fhand = open('movie_quotes.txt')
    contents = fhand.read()
    print contents
    fhand.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    #open a connection to a site on the internet then read a response from that website
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=shot'+ text_to_check)
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


