import random
import string

adjectives = ["sleepy", "slow", "smelly",
              "wet", "fat", "sweaty",
              "thin", "tired", "active",
              "surprised", "playful", "fluffy",
              "hardworking", "proud", "brave"]

nouns = ["apple", "dinosaur", "ball",
         "toaster", "goat", "dragon",
         "hammer", "duck", "panda",
         "telephone", "banana", "teacher"]

colors = ["black", "red", "orange",
          "yellow", "green", "blue",
          "indigo", "violet", "white"]

print("Welcome to Password Picker!")

while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        color = random.choice(colors)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + color + str(number) + special_char
        print("Your new password is: %s" % password)

    response = input("Would you like another password? Type y or n: ")
    if response == "n":
        break
