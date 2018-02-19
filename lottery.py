import random

def lottery(numbers):
    lottery_numbers = []
    counter = 0
    while counter != numbers:
        random_num = random.randint(1,90)
        if random_num not in lottery_numbers:
            lottery_numbers.append(random_num)
            counter += 1
    return lottery_numbers

def bet(numbers):
    bets = []
    counter = 0
    print "Please take your bet! 1-90 What is your %s number?" % (numbers)
    while counter != numbers:
        bet = raw_input(str(counter + 1) + ".: ")
        if (int(bet) not in bets) and ((int(bet) >= 1) and (int(bet) <= 90)):
            bets.append(int(bet))
            counter += 1
        else:
            if int(bet) in bets:
                print "You have already bet " + bet + " choose another number!"
            else:
                print "Out of range please choose 1-90"
    return bets

def main():

    print "Welcome to the Lottery numbers generator."
    numbers = int(raw_input("Please enter how many random numbers would you like to have: "))
    your_bet = bet(numbers)
    winnig_numbers = lottery(numbers)
    print "Your numbers:"
    print(your_bet)
    print "And a winning numbers are:"
    print(winnig_numbers)
    match = set(your_bet).intersection(set(winnig_numbers))
    if len(match) == numbers:
        print list(match) + "JACKPOT!! YOU WIN AMAZING!!!"
    elif len(match) == 0:
        print "Sorry, you don't have any hit, better luck next time!"
    else:
        print "Congratulations you hit " + str(len(match)) + " " + list(match)

if __name__ == "__main__":
    main()