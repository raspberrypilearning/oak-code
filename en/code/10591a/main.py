print("Welcome to the FizzBuzz Game!")
print("----------------------------------")
print("You will choose a range of numbers.")
print("The game will print 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, and 'FizzBuzz' for multiples of both!")
print("----------------------------------")

# Part 2: Get number of plays
while True:
    try:
        plays = int(input("How many times would you like to play? "))
        if plays > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Error: Please enter a whole number.")

# Repeat the game for the number of plays
for play in range(plays):
    print(f"\nGame {play + 1}")

    # Part 3: Get start and end numbers
    while True:
        try:
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            if start < end:
                break
            else:
                print("Start number must be less than end number.")
        except ValueError:
            print("Error: Please enter whole numbers only.")

    # Part 4: Loop through the range and apply FizzBuzz rules
    for number in range(start, end + 1):
        try:
            output = ""
            if number % 3 == 0:
                output += "Fizz"
            if number % 5 == 0:
                output += "Buzz"
            if output == "":
                output = str(number)
            print(output)
        except TypeError:
            print("Type Error: An unexpected problem occurred.")

print("\nThanks for playing FizzBuzz!")