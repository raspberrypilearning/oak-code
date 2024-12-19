import random

print("Welcome to rock, paper, scissors")

# Ask the player for their choice
player1 = input("Enter rock (r), paper (p) or scissors (s):")

# The computer generates a random choice
player2 = random.choice(["r", "p", "s"])
print(f"The computer chose {player2}")

# Use Boolean logic to compare the choices
if player1 == player2:
    print("Draw")

# Winning
elif (
    (player1 == "r" and player2 == "s")
    or (player1 == "p" and player2 == "r")
    or (player1 == "s" and player2 == "p")
):
    print("You win")

else:
    print("You lose")
