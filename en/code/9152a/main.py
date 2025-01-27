import random

cards = [2, 5, 7, 6, 10, 3, 9]
random.shuffle(cards)
guess = False
picked = random.choice(cards)
while guess != True:
    print("Guess the card")
    card_picked = int(input())
    if card_picked == picked:
        print("You guessed correctly")
        guess = True
    else:
        print("Try again")
        if card_picked < picked:
            print("The card is higher")
        elif card_picked > picked:
            print("The card is lower")
