print("Where do you live?")
location = input()
print("Weather in", location, "now?")
weather = input()

### Add code below

if weather == "cloudy":
  advice = "No sunglasses"
elif weather == "rainy":
  advice = "Get an umbrella"
elif weather == "snowy":
  advice = "Gloves and earmuffs"
else:
  advice = "No particular advice"
print(advice)
