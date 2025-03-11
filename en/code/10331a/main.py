print("Welcome to the sandwich shop")
print("-----------------------------")
print("Sandwich prices:")
print("-------------------------------------------")
print("Sandwiches              Wraps")
print("-------------------------------------------")
print("Sandwich       £2.80    Wrap          £3.00")
print("With crisps    +30p     With crisps    +30p")
print("-------------------------------------------")
total = 0
print("Would you like a sandwich or a wrap?: ")
choice = input()
if choice == "sandwich":
    total = total + 2.80
else:
    total = total + 3.00
print("Would you like crisps with your order? (y/n): ")
crisps = input()
if crisps == "y":
    total = total + 0.30
    total = round(total,2)
print(f"The total of your order is £{total}")
if total >= 3.00:
    print("You have earned a sandwich stamp.")