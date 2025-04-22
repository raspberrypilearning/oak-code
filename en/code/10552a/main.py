import random
import string

num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = 8
characters = string.ascii_letters + string.digits

print("Generated passwords:")

for password_num in range(num_passwords):
    password = ""  
    for _ in range(password_length):
        random_char = random.choice(characters)
        password = password + random_char

    print(password)