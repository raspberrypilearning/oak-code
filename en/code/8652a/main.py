correct_passcode = "1234"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    passcode = input("Enter passcode: ")
    attempts += 1

    if passcode == correct_passcode:
        print("Phone unlocked!")
        attempts = max_attempts  
    elif attempts == 1:
        print("Incorrect passcode. Try again. Hint: The passcode has 4 digits.")
    else:
        print("Incorrect passcode. Try again.")

if attempts == max_attempts and passcode != correct_passcode:
    print("Too many attempts. Phone locked.")