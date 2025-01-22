from textfile import load
rainfall_data = load("rainfall_data.txt")
count = 0
for value in rainfall_data:
    if value > 65:
        count = count + 1

print(f"Number of times rainfall exceeds 65mm: {count}")

