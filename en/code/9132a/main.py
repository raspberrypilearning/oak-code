from random import choice

cities = ["Athens","Berlin", "Brussels","Copenhagen",
          "Dublin","London","Madrid","Paris",
          "Prague","Stockholm","Vienna"]

city = choice(cities)
done = False

while done == False:
  print("Guess the capital:")
  guess = input()
  if guess == city:
    print("You've got it!")
    done = True
  elif guess == "":
    print(f"It was {city}")
    done = True
  elif city[0] != guess[0]:
    print(f"The first letter is: {city[0]}")
  elif len(guess) != len(city):
    print(f"It has {len(city)} letters")
  elif city[1] not in guess:
    print(f"It contains letter {city[1]}")
  else:
    print("Try again")
