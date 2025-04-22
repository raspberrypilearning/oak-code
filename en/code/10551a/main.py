from random import randint
from time import sleep

user_number = int(input("Enter a number between 1 and 10: "))
print(f"Your number is {user_number}")

print("I am generating a random number...")
sleep(2)

random_number = randint(1, 10)
print(f"My random number is: {random_number}")