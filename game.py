#importe
import datetime
import json
import random

#Variablen
player = input("Hi, what is your name? ")
playing = True
secret = random.randrange (1, 21)
tries = 0
guess = 0

#Funktionen

#Spiel wiederholen
def playagain():
    answer = input("Do you want to play again? Type [y/n]. ")
    if (answer.strip() == "y"):
        playing = True
        secret = random.randrange(1, 21)
        tries = 0
        guess = 0

        while guess != secret:
            guess = int(input("Welcome! Make a guess for a number between 1 and 20: "))
            if guess > secret:
                print("Too high.. try it again!")
                tries = tries + 1
            elif guess < secret:
                print("Too low.. try it again!")
                tries = tries + 1
            else:
                print("You got it! Congratulations!")
                score_list.append({"tries": tries, "date": str(datetime.datetime.now()), "player": player,
                                   "secret": secret})

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

        print("These are your number of tries:", tries)
        playing = playagain()

    elif (answer.strip() == "n"):
        print("Alright! Thank you for playing!")
    else:
        return playagain()

#Scorelist
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

#Game
while guess != secret:
    guess = int(input("Welcome! Make a guess for a number between 1 and 20: "))
    if guess > secret:
        print("Too high.. try it again!")
        tries = tries + 1
    elif guess < secret:
        print("Too low.. try it again!")
        tries = tries + 1
    else:
        print("You got it! Congratulations!")
        score_list.append({"tries": tries, "date": str(datetime.datetime.now()), "player": player,
                           "secret": secret})

    with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

print("These are your number of tries:", tries)
playing = playagain()

