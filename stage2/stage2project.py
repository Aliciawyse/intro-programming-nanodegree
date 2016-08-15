#Define functions once at the top of this script

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
    
def play_game(ml_string, parts_of_speech):    
    replaced = []
    print "The current paragraph reads as such:\n", ml_string
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("\nType in your guess for " + replacement + ": ")
            word = word.replace(replacement, user_input)
            replaced.append(" " + word)
            index = len(" ".join(replaced))
            print "\nThe current paragraph reads as such:\n", " ".join(replaced), " ".join(ml_string[index:])
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