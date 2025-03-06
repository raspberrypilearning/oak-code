print("What is your name?")
name = input().lower() 
if name == "laura":
  print("How do you do Laura!")
else:
  print(f"Nice name, {name}")

print(f"So {name}, how are you today")
feeling = input().upper()
if feeling == "GOOD":
  print("Great, I'm glad you are good!")
elif feeling == "BAD":
  print("Oh no, I'm sorry to hear you feel bad")
else:
  print("Sorry, I don't understand how you feel")

print("What is your favourite colour?")
colour = input().lower()
if colour == "blue":
  print("Blue is my favourite too")
else:
  print("That is not my favourite colour")

print("What is the weather like where you are today?")
weather = input().lower()
if weather == "rainy":
  print("Wear a coat")
elif weather == "sunny":
  print("Wear sun cream")
else:
  print("I have no advice")

print("Have a good day! Bye!")