# print("\n                 ==========Day 7==========")
# print("\n                 ==========Hangman==========")

# #!  _
# #! | |
# #! | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# #! | '_ \ / _` | '_ \ / _` | '_ ` _  \/ _` | '_ \  
# #! | | | | (_| | | | | (_| | | | | | | (_| | | | |
# #! |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
# #!                     __/ |
# #!                    |___/

logo1 = '''

  _
 | |
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
 | '_ \ / _` | '_ \ / _` | '_ ` _  \/ _` | '_ \  
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
    '''
print(logo1)       


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random
chosen_word = random.choice(word_list)
print(chosen_word)
word_list = list(chosen_word)
guess = str(input("Guess a letter: "))
guess = guess.lower()
for x in word_list:
    if x == guess:
        print("Right")
    else:
        print("Wrong")