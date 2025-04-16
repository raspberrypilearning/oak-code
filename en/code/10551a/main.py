import random
import time

user_number = int(input("Enter a number between 1 and 10: "))
print(f"Your number is {user_number}")

print("I am generating a random number...")
time.sleep(2)

random_number = random.randint(1, 10)
print(f"My random number is: {random_number}")