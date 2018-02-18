import random

def main():
    play_more = "y"
    secret = random.randint(1,30)
    life = 5
    score ={"WINS" : 0, "LOSSES" : 0}
    while play_more.lower() == "y" and life > 0:
        guess = int(raw_input("Guess the secret number (between 1 and 30): "))
        if guess == secret:
            score["WINS"] += 1
            print "You guessed it - congratulations! It's number %s :)" % (secret)
            play_more = raw_input("Want to play more? y/n ")
            if play_more.lower() != "y":
                print "GAME OVER"
                print score
                break
            else:
                secret = random.randint(1, 30)
                life = 5
        elif guess > secret:
            life -= 1
            print "Try smaller, you have " + str(life) + " more guesses"
        else:
            life -= 1
            print "Try bigger, you have " + str(life) + " more guesses"
        if life == 0:
            score["LOSSES"] += 1
            print "Sorry you have no more guesses. My secret number was %s" % (secret)
            play_more = raw_input("Want to try again? y/n")
            if play_more.lower() != "y":
                print "GAME OVER"
                print score
                break
            else:
                secret = random.randint(1, 30)
                life = 5

if __name__ == "__main__":
    main()