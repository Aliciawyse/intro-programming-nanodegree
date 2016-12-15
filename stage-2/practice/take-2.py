def word_in_pos(word, parts_of_speech):
    for item in parts_of_speech:
        if item in word: 
            return word
        #return none outside of the for loop since we want to first compare word to every word in parts_of_speech
        return None

ml_string = """I pledge allegiance to the __1__ of the United States of __2__, and to the republic for which it stands, one nation under God, __3__, with liberty and __4__ for all."""  
parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]

def play_game(ml_string, parts_of_speech):
    
    #Create an empty string that will be used to build out the updated madlib.
    replaced = []
    
    #Show user what the paragraph looks like. 
    print "The current paragraph reads as such:\n", ml_string
    
    #Convert ml_string into a list.
    ml_string = ml_string.split()

    #Use an iterative variable since the user can only make limited amount of guesses.
    #count = 0
    
    while True: 
        for word in ml_string:
            replacement = word_in_pos(word, parts_of_speech)
            if replacement != None:
                
                #Prompt user to make a guess.
                user_input = raw_input("\nType in your guess for " + replacement + ": ")
                    
                #Update the replacement variable with the users input
                #and stick it in the word variable
                word = word.replace(replacement, user_input)
    
                #Append a space and the word to the empty list
                replaced.append(" " + word)
                
                #If the result is NONE append the element from ml_string 
                #that we're currently dealing with to the empty list replaced,
                
                continue
            else:
                replaced.append(" " + word)
                continue
    
    #replaced has the same structure as ml_string only that the replacement words are swapped with user input
    replaced = "".join(replaced)
    return replaced

print play_game(ml_string, parts_of_speech)