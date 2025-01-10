from random import choice

cities = ["Athens","Berlin", "Brussels","Copenhagen",
          "Dublin","London","Madrid","Paris",
          "Prague","Stockholm","Vienna"]

city = choice(cities)
done = False

while not done:
  print("Guess the capital:")
  guess = input()
  if guess == city:
    print("You've got it!")
    done = True
  elif guess == "":
    print("It was", city)
    done = True
  else:
    print("Try again")
