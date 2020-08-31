import random
import datetime

# Model for OOP
class Result:
    def __init__(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.date = date


# Loop function for playing the game.
def play_game(level="easy"):
    player = input("Player name: ")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the secret number between 1 and 100: "))
        attempts += 1

        if guess == secret:
            new_result = Result(
                player_name=player,
                score=attempts,
                date=datetime.datetime.now()
            )

            with open("results.txt", "w") as results_file:
                results_file.write(str(new_result.__dict__))
            print("You've guessed the secret number! It's number: " + str(secret) + " Good job! ;)")
            print("Attempts needed: " + str(attempts))
            break
        elif guess < secret and level == "easy":
            print("Try something bigger! :)")
        elif guess > secret and level == "easy":
            print("Try something smaller! :)")
        else:
            print("Your guess is incorrect. Try again ;)")


while True:
    selection = input("Would you like to: \n"
                      "P) play a game, \n"
                      "Q) quit the game: \n")

    if selection.upper() == "P":
        level = input("Choose your level (easy/hard): ")
        play_game(level=level)
    else:
        break