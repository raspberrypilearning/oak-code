from textfile import load
rainfall_data = load("rainfall_data.txt")
max_rainfall = 0
min_rainfall = 100
for value in rainfall_data:
    if value > max_rainfall:
        max_rainfall = value
    elif value < min_rainfall:
        min_rainfall = value

print(f"Maximum rainfall in mm: {max_rainfall}" )
print(f"Minimum rainfall in mm: {min_rainfall}" )