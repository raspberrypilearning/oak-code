x = "sandwich"
y = ""
z = x != y
a = 0

while z and a < 5:
    print("Guess the word: ")
    y = input()
    if y == x:
        a = a + 1
        b = "CORRECT!"
        z = False
    else:
        a = a + 1
        b = "INCORRECT!"

print(f"You were {b}. Guesses: {a}")