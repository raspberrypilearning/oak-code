word = "sandwich"
guess = ""
not_guessed = word != guess
guesses = 0

# continue to guess whilst incorrect and number of guesses less than 5

while not_guessed and guesses < 5:
    guess = input("Guess the word: ")
    if guess == word:
        guesses += 1
        result = "CORRECT!"
        not_guessed = False
    else:
        guesses += 1
        result = "INCORRECT!"

# display the final result to the user
print("You were", result, "Guesses:", guesses)