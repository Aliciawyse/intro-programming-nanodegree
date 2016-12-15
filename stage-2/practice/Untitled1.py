
#Define functions once, at the top of this script

#This function has two inputs, word & parts_of_speech. 
#Parts_of_speech is a list. It contains words we want to replace.
#Word is a string that will contain a substring from the parts_of_speech list.
#If there is an element in parts_of_speech list that is in the word, then return that parts_of_speech element, else return None. 
#We use this function in our madlibs game/the play_game function.

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
    
#This function has two inputs, ml_string and parts_of_speech. Ml_string is a string that contains replacement words found in parts_of_speech. Parts_of_speech is a list of replacement words. We create an empty list called replaced. It well be used to construct an updated madlib.

#We convert ml_string into a list. Using a for loop we can traverse ml_string. 

#The for loop tells the computer, for each element in ml_string: 1)Create a variable called replacement to hold the result of the function above when we pass through an element from ml_string. 2)If the result is NONE append the element from ml_string that we're currently dealing with to the empty list replaced, but if the result is NOT none, ask the user to make a guess. Then take the element from ml-string that we're currently dealing with and replace it with the user's input. Afterwards, append our updated ml_string element to the empty list called replaced. 

#Once we exit the for loop, we turn our list called replace into a string using pythons built-in join method. Then we return replaced. 

#& the function about, we can check if (any part of) the current iteration of ml_string is in parts_of_speech. If it is, we replace the word with the users input and add it to an empty list called replaced. 
    
    
def play_game(ml_string, parts_of_speech):    
    replaced = []
    print "The current paragraph reads as such:\n", ml_string
    ml_string = ml_string.split()
    count = 0
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("\nType in your guess for " + replacement + ": ")
            word = word.replace(replacement, user_input)
            replaced.append(" " + word)
            count = count + 1
            if count != 4:
                print "\nThe current paragraph reads as such:\n", "".join(replaced)," ".join(ml_string[len(replaced):])
        else:
            replaced.append(" " + word)
    replaced = "".join(replaced)
    return replaced

#Create a while loop for each difficulty level.

#If user enters input that's invalid, the following code will run. 
while True:
    
    choice = raw_input("Welcome to Alicia's madlib games. Please type in a difficulty level. Your options are: easy, medium and hard. ")
    
    if choice not in ["easy", "medium", "hard"]:
        print "Please enter a valid option."
    if choice in ["easy", "medium", "hard"]:
        break

#if user chooses the easy option, the following code will run. 
while choice == "easy":
    print "Easy level - here we go!\n"
        
    parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
    ml_string = """Life is like a __1__ of __2__. You __3__ know what you are gonna __4__."""
    
    print play_game(ml_string, parts_of_speech)
    break

#if user chooses the medium option, the following code will run.
while choice == "medium":
    print "Medium level - here we go!\n"
        
    parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
    ml_string = """That's one small __1__ for __2__, one __3__ giant step for __4__."""
    
    print play_game(ml_string, parts_of_speech)
    break

#if user chooses the hard option, the following code will run. 
while choice == "hard":
    print "Hard level - here we go!\n"
        
    parts_of_speech  = ["__1__", "__2__", "__3__", "__4__","__5__"]
    ml_string = """Give a man a __1__ and you __2__ him for a day; __4__ a man to fish and you feed him for a __5__."""
    
    print play_game(ml_string, parts_of_speech)
    break

print "\n Thanks for playing!"
