""" A quiz game based on animals
The player is asked a few questions about animals and
scores are given if passed
"""

def check_guess(guess, answer):
    """
    checks the answers provided for the guess and determines the score
    """
    global score  # identifies the score variable as nonlocal
    # sets the number of guesses per question
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:  # loop for num of guesses, maximum guess is 2
        if guess.lower() == answer.lower():  # compare guess to answer(and sets all inputs to lower case)
            print("Correct answer")
            # determines the point given per attempt
            score += 3 - attempt
            score += 1
            still_guessing = False
        else:
            # calculates the number of attempts and prints a warning message
            if attempt < 1:
                guess = input("Sorry wrong answer. Try again. ")
            attempt += 1
# prints the correct answer after 2 attempts
    if attempt == 2:
        print("The correct answer is " + answer)


score = 0  # used to keep track of the animal
print("Guess the Animal!")  # Introduces the game to the player

# main game area for the guessing
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "cheetah")
guess3 = input("Which is the largest animal? ")
check_guess(guess3, "blue whale")
guess4 = input("Which animal has a long trunk? ")
check_guess(guess4, "elephant")
guess5 = input("What kind of mammal can fly? ")
check_guess(guess5, "bat")
guess6 = input("How many hearts does an octopus has? ")
check_guess(guess6, "3")
guess7 = input("Which onw of this is a fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid.\n Type A, B, C, or D.\n")
check_guess(guess7, "C")
guess8 = input("Mice are mammals. True or False? ")
check_guess(guess8, "True")
# displays the player's score
print("Your score is " + str(score))
