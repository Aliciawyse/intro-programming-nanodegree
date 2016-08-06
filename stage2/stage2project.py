while True:
    choice = raw_input("Welcome to Alicia's madlib games. Please type in a difficulty level. Your options are: easy, medium and hard. ")
    
    if choice not in ["easy", "medium", "hard"]:
        print "Please enter a valid option."
    
    if choice == "easy":
        print "Easy level - here we go!\n"
        
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        ml_string = """Life is like a __1__ of __2__. You __3__ know what you are gonna __4__."""
        
        def word_in_pos(word, parts_of_speech):
            for pos in parts_of_speech:
                if pos in word:
                    return pos
            return None
                
        def play_game(ml_string, parts_of_speech):    
            replaced = []
            ml_string = ml_string.split()
            for word in ml_string:
                replacement = word_in_pos(word, parts_of_speech)
                if replacement != None:
                    user_input = raw_input("Type in a " + replacement + ": ")
                    word = word.replace(replacement, user_input)
                    replaced.append(" " + word)
                else:
                    replaced.append(" " + word)
            replaced = "".join(replaced)
            return replaced
    
        print play_game(ml_string, parts_of_speech)
        break

    if choice == "medium":
        
        print "Medium level - here we go!\n"
        
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        ml_string = """That's one small __1__ for __2__, one __3__ giant step for __4__."""
        
        def word_in_pos(word, parts_of_speech):
            for pos in parts_of_speech:
                if pos in word:
                    return pos
            return None
                
        def play_game(ml_string, parts_of_speech):    
            replaced = []
            ml_string = ml_string.split()
            for word in ml_string:
                replacement = word_in_pos(word, parts_of_speech)
                if replacement != None:
                    user_input = raw_input("Type in a " + replacement + ": ")
                    word = word.replace(replacement, user_input)
                    replaced.append(" " + word)
                else:
                    replaced.append(" " + word)
            replaced = "".join(replaced)
            return replaced
    
        print play_game(ml_string, parts_of_speech)
        break

    if choice == "hard":

        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__","__5__"]
        ml_string = """Give a man a __1__ and you __2__ him for a day; __4__ a man to fish and you feed him for a __5__."""
        
        def word_in_pos(word, parts_of_speech):
            for pos in parts_of_speech:
                if pos in word:
                    return pos
            return None
                
        def play_game(ml_string, parts_of_speech):    
            replaced = []
            ml_string = ml_string.split()
            for word in ml_string:
                replacement = word_in_pos(word, parts_of_speech)
                if replacement != None:
                    user_input = raw_input("Type in a " + replacement + ": ")
                    word = word.replace(replacement, user_input)
                    replaced.append(" " + word)
                else:
                    replaced.append(" " + word)
            replaced = "".join(replaced)
            return replaced
    
        print play_game(ml_string, parts_of_speech)
        break

print "Thanks for playing."