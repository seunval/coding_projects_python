# Guessing game
""" Rules::: Choose difficulty levels betweeen easy, normal and hard to determine number of lives
            guess the word if you can or guess each character to get a clue of the word
            and type it in full before the list fills up
"""

import random  # import random module for random selection

lives = 9  # number of lives
# list of words to be guessed
words = ["pizza", "fairy", "teeth",
         "shirt", "otter", "plane",
         "brush", "horse", "light"]

secret_word = random.choice(words)  # randomly choose words from the words list
# clue = list("?????")
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index += 1

heart_symbol = u'\u2764'  # stores the ascii heart symbol code in the variable
guessed_word_correctly = False  # sets flag for correct guess to False
unknown_letters = len(secret_word)  # stores the length of the chosen word into unknown_letters


def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    """
    stores user input in guessed_letter,
    compares it with the randomly chosen word stored in the secret_word variable,
    stores the correct input in the corresponding index of clue list,
    decreases the length of the unknown_letters by 1 and then returns unknown_letters
    """
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters -= 1
        index += 1

    return unknown_letters


# asks player to input difficulty level and stores it as an integer in difficulty
difficulty = int(input("Choose difficulty (type 1, 2, or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n"))
# determines number of live per difficulty
if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 6

while lives > 0:
    print(clue)
    print("Lives left: " + heart_symbol * lives)
    guess = input("Guess a letter or the whole word: ")
    # compares guess to chosen word and changes flag to true if correct
    if guess == secret_word:
        guessed_word_correctly = True
        break

    # checks if guessed character is in chosen word and reduces the unknown_letters if found
    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    # reduces number of lives if guess is wrong
    else:
        print("Incorrect. You loose a life.")
        lives -= 1

# if all unknown_letters are found,
# flag for correctly guessed word changes to true and game ends
if unknown_letters == 0:
    guessed_word_correctly = True

# prints a winning msg if user wins
if guessed_word_correctly:
    print("You Won! The secret word was " + secret_word)

# prints a losing msg if user losses
else:
    print("You lost! The secret word was " + secret_word)
