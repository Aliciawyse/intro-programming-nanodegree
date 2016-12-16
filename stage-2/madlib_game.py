def word_in_pos(word, parts_of_speech):
    for item in parts_of_speech:
        if item in word: 
            return word
    return None 

def play_game(ml_string, parts_of_speech):  
    
    print ("The current paragraph reads as such:\n", ml_string)

    ml_string = ml_string.split()
    replaced = []

    for word in ml_string:

        replacement = word_in_pos(word, parts_of_speech)

        if replacement != None:

            while True:
                user_input = input("\nType in your guess for " + replacement + ": ")
                count = 0

                if user_input not in answers:
                    count += 1
                    print ("Sorry, that's wrong. Try again!")
                    continue
                    
                else:
                    break

            word = word.replace(replacement, user_input)
            replaced.append(" " + word)
            count = count + 1                
                        
            print ("\nThe current paragraph reads as such:\n", "".join(replaced)," ".join(ml_string[len(replaced):]))

        else:
            replaced.append(" " + word)

    replaced = "".join(replaced)
    return replaced


while True:
    user_difficulty_level = input("Welcome to Alicia's madlib games. Please type in a difficulty level. Your options are: easy, medium or hard. ")

    if user_difficulty_level not in ["easy", "medium", "hard"]:
        print ("\nPlease enter a valid level option\n")
        continue
    
    if user_difficulty_level == "easy":
        
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        ml_string = """I pledge allegiance to the __1__ of the United States of __2__, and to the republic for which it stands, one nation under God, __3__, with liberty and __4__ for all."""  

        answers = ["flag", "America", "indivisible", "justice"]

        play_game(ml_string, parts_of_speech)

        print ("\n You did it! Great Job!")
        break

    if user_difficulty_level == "medium":
        
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        ml_string = """Standard __1__ is a measure of __2__ of a set of __3__ from its __4__."""  

        answers = ["deviation", "dispersion", "data", "mean"]

        play_game(ml_string, parts_of_speech)

        print ("\n You did it! Great Job!")
        break

    if user_difficulty_level == "hard":
        
        parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]
        ml_string = """The __1__ annual __2__ rate is the interest rate that is actually earned or paid on an investment due to __3__ over a given period of __4__."""
        
        answers = ["effective", "interest", "compounding", "time"]

        play_game(ml_string, parts_of_speech)

        print ("\n You did it! Great Job!")
        break


