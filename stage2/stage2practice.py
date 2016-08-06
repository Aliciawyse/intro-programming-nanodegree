#Create a function. The function should be called word_in_pos. The function has two inputs:
# 1) a string and 2) a list

#For ALL elements in parts_of_speech, check if the element is in a string. If element is in string return the element. Note, parts_of_speech is a list of words we want to replace, eventually, with user input.

test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

def word_in_pos(a_string, a_list):
    for word in parts_of_speech:
        if word in a_string:
            return word
    else:
        return None

print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)



