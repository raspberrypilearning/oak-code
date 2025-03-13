print("Welcome to the sandwich shop")
print("-----------------------------")
print("Sandwich prices:")
print("-----------------------------------------------------------------")
print("Sandwiches                           Wraps")
print("-----------------------------------------------------------------")
print("Sandwich (meat filling)    £2.80     Wrap (meat filling)    £3.00")
print("Sandwich (veg filling)     £2.50     Wrap (veg filling)     £2.70")
print("With crisps                  +30p    With crisps             +30p")
print("-----------------------------------------------------------------")
total = 0
print("Would you like a sandwich or a wrap?: ")
choice = input()
print("Would like meat or veg filling? (m/v): ")
filling = input()
if choice == "sandwich" and filling == "m":
    total = total + 2.80
elif choice == "sandwich" and filling == "v":
    total = total + 2.50
elif choice == "wrap" and filling == "m":
    total = total + 3.00
else:
    total = total + 2.70
print("Would you like crisps with your order? (y/n): ")
crisps = input()
if crisps == "y":
    total = total + 0.30
    total = round(total,2)
print(f"The total of your order is £{total}")