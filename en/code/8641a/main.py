print("What is the weather like now?")
weather = input()

### Add code below

if weather == "cloudy":
  advice = "No sunglasses"
elif weather == "rainy":
  advice = "Get an umbrella"
elif weather == "snowy":
  advice = "Gloves and earmuffs"
else:
  advice = "Enjoy the day!"
print(advice)
