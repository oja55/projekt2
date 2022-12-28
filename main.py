"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Bulls & Cows

author: Ondřej Vítek
email: ondra5510@gmail.com
discord: oja55#8858
"""

import random

short_line = 47 * "-"


def generate_number():
    numbers = [str(i) for i in range(1, 10)]
    random.shuffle(numbers)
    return "".join(numbers[:4])


def get_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def play_game():
    secret = generate_number()

    print("Hi there!",
          short_line,
          "I've generated a random 4 digit number for you.",
          "Let's play a bulls and cows game.",
          short_line,
          sep="\n"
          )

    guess_count = 0
    while True:
        guess = input("Enter your number: ")
        if not guess.isdigit():
            print("It's not a number.")
        elif guess.startswith("0"):
            print("Number can't start with 0")
        elif len(guess) > 4:
            print("Number is too long.")
        elif len(guess) < 4:
            print("Number is too short.")
        elif len(guess) != len(set(guess)):
            print("Number has duplicates.")
        else:
            bulls, cows = get_bulls_and_cows(secret, guess)
            guess_count += 1
            print(f"Bulls: {bulls}, Cows: {cows}",
                  short_line,
                  sep="\n")

            if bulls == 4:
                print(f"Correct, you've guessed the right number\nin {guess_count} guesses!",
                      short_line,
                      sep="\n")
                if guess_count <= 4:
                    print("That's amazing!")
                    break
                elif guess_count <= 7:
                    print("That's average.")
                    break
                elif 8 <= guess_count:
                    print("That's not so good.")
                    break


play_game()
