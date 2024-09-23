# password generator by randomly selecting from lists of
# adjectives, nouns, colors, digits and special characters

# import necessary libraries
import random
import string

# list of adjectives
adjectives = ["sleepy", "slow", "smelly",
              "wet", "fat", "sweaty",
              "thin", "tired", "active",
              "surprised", "playful", "fluffy",
              "hardworking", "proud", "brave"]

# list of nouns
nouns = ["apple", "dinosaur", "ball",
         "toaster", "goat", "dragon",
         "hammer", "duck", "panda",
         "telephone", "banana", "teacher"]

# list of colors
colors = ["black", "red", "orange",
          "yellow", "green", "blue",
          "indigo", "violet", "white"]

print("Welcome to Password Picker!")

while True:  # infinite loop for user inputs
    for num in range(3):  # loop through choices 3 times
        # random selections between adjectives, nouns and colors
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        color = random.choice(colors)
        number = random.randrange(0, 100)  # randomly pick numbers from 0 to 100
        special_char = random.choice(string.punctuation)  # randomly select punctuations from string library

        # concatenate all random selections and print the output
        password = adjective + noun + color + str(number) + special_char
        print("Your new password is: %s" % password)

        # asks for user input to generate new password
    response = input("Would you like another password? Type y or n: ")
    if response == "n":
        break  # break infinite loop
