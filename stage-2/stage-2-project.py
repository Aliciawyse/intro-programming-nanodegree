#Our word_in_pos function takes in a string (word) and a list (parts_of_speech).
#If there is a word in parts_of_speech that is a substring of the string word -- return that word, else return none.

def word_in_pos(word, parts_of_speech):
    for item in parts_of_speech:
        if item in word: 
            return word
        #return none outside of the for loop since we want to first compare word to every word in parts_of_speech
        return None 
    
#Our play_game function has two inputs.
#parts_of_speech which is a list of acceptable replacement words and ml_string is a string which can contain replacement words found in parts_of_speech.
#The words in ml_string that we want to replace with user input are "__1__", "__2__", "__3__", "__4__"

def play_game(ml_string, parts_of_speech):  
    
    while True:
        
        #Show user what the paragraph looks like. 
        print "The current paragraph reads as such:\n", ml_string
    
        #Convert ml_string into a list.
        ml_string = ml_string.split()
    
        #Use an iterative variable since the user can only make limited amount of guesses.
        count = 0
    
        #Create an empty string that will be used to build out the updated madlib.
        replaced = []
    
        for word in ml_string:
            replacement = word_in_pos(word, parts_of_speech)

            if replacement != None:
                
                #Prompt user to make a guess.
                user_input = raw_input("\nType in your guess for " + replacement + ": ")
                
                #Update the replacement variable with the users input
                #and stick it in the word variable
                word = word.replace(replacement, user_input)
            
            #if word not in answers:
            #    continue
                
                #Append a space and the word to the empty list
                replaced.append(" " + word)
            
                #Keep track of the number of times a user makes a guess
                count = count + 1
            
                #Print an updated version of the madlib by converting replaced to a string
                #and concatonating it with the rest of the madlib that we havent addressed yet
                if count != 4:
                    print "\nThe current paragraph reads as such:\n", "".join(replaced)," ".join(ml_string[len(replaced):])
        
            #If the result is NONE append the element from ml_string 
            #that we're currently dealing with to the empty list replaced,
            else:
                replaced.append(" " + word)
    
    #replaced has the same structure as ml_string only that the replacement words are swapped with user input
    replaced = "".join(replaced)
    return replaced



#If user enters input that's invalid, the following code will run. 
while True:
    
    choice = raw_input("Welcome to Alicia's madlib games. Please type in a difficulty level. Your options are: easy, medium and hard. ")
    
    if choice not in ["easy", "medium", "hard"]:
        print "Please enter a valid option."
    if choice in ["easy", "medium", "hard"]:
        break

#Create a while loop for each difficulty level.

parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]

while choice == "easy":
    print "Easy level - here we go!\n"
    
    ml_string = """I pledge allegiance to the __1__ of the United States of __2__, and to the republic for which it stands, one nation under God, __3__, with liberty and __4__ for all."""  
        
    answers = ["flag", "America", "indivisible", "justice"]

    
    print play_game(ml_string, parts_of_speech)
    break

while choice == "medium":
    print "Medium level - here we go!\n"
        
    ml_string = """That's one small __1__ for __2__, one __3__ leap for __4__."""
    
    answers = ["step", "man", "giant", "mankind"]

    print play_game(ml_string, parts_of_speech)
    break

while choice == "hard":
    print "Hard level - here we go!\n"
        
    ml_string = """Hello __1__."""
    
    answers = ["world"]

    print play_game(ml_string, parts_of_speech)
    break

print "\n Thanks for playing!"