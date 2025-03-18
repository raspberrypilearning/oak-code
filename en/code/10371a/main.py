score = 0
print("Guess the punchline...")
print("What is pink and fluffy?")
pink_joke = input().upper()
if pink_joke == "PINK FLUFF":
  print("You got it! 1 point")
  score = score + 1
else:
  print("Wrong, it was Pink Fluff")
print("Guess the punchline...")
print("What is brown and sticky?")
stick_joke = input().upper()
if stick_joke == "A BROWN STICK":
  print("You got it! 1 point")
  score = score + 1
elif stick_joke == "BROWN STICK":
  print("You got it! 1 point")
  score = score + 1
else:
  print("Wrong, it was A brown stick")
print("Guess the punchline...")
print("What is black and white and red all over?")
red_joke = input().upper()
if red_joke == "A NEWSPAPER":
  print("You got it! 1 point")
  score = score + 1
elif red_joke == "NEWSPAPER":
  print("You got it! 1 point")
  score = score + 1
else:
  print("Wrong, it was A Newspaper")
print(f"Your score is {score}")