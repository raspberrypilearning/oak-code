from random import randint 
num1 = 3
num2 = randint(2,12)
print(f"{num1} times {num2} =")
answer = int(input())
product = num1 * num2
if answer == product:
  print("That is correct")
else:
  print("I am sorry")
  print(f"{num1} times {num2} is {product}")