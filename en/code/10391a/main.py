#print menu and prices to user
print("Welcome to the sandwich shop")
print("-----------------------------")
print("Sandwich prices:")
print("-----------------------------------------------------------------")
print("                      Sandwich       Wrap")
print("-----------------------------------------------------------------")
print("1. Chicken            £2.80          £3.00")
print("2. Ham                £2.50          £2.70")
print("3. Cheese             £2.10          £2.30")
print("4. Tuna & Sweetcorn   £2.10          £2.30")
print("5. Hummus & Avocado   £2.90          £3.10")
print("6. Falafel            £2.90          £3.10")
print("With crisps             +30p          +30p")
print("With drink            £1.00          £1.00")
print("-----------------------------------------------------------------")
total = 0
print("Would you like a sandwich or a wrap?: ")
type = input()
print("Which filling would you like (1-6)?: ")
filling = int(input())

if type == "sandwich":
    if filling == 1:
        total = total + 2.8
    elif filling == 2:
        total = total + 2.5
    elif filling == 3 or filling == 4:
        total = total + 2.10
    elif filling == 5 or filling == 6:
        total = total + 2.90
    else:
        print("You have not entered a valid filling option")

elif type == "wrap":
    if filling == 1:
        total = total + 3
    elif filling == 2:
        total = total + 2.7
    elif filling == 3 or filling == 4:
        total = total + 2.30
    elif filling == 5 or filling == 6:
        total  = total + 3.10
    else:
        print("You have not entered a valid filling option")

print("Would you like crisps with your order? (y/n): ")
crisps = input()
if crisps == "y":
    total = total + 0.30

print("Would you like a drink with your order? (y/n): ")
drink = input()
if drink == "y":
    total = total + 1

print(f"The total of your order is £{total}")

if total > 4:
    print("You have earned a sandwich stamp!")