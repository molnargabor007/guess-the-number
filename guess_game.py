secret = 15

guess = int(raw_input("Guess the number between 1 and 30: ").strip())

while guess != secret:
    guess = int(raw_input("Sorry, that is not my number, try agian: ").strip())
    if guess == secret:
        print "Congratulations! You WIN! the number is: ", guess

secret = 22

