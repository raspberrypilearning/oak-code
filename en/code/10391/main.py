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

#take in users choices
total = 0
print("Would you like a sandwich or a wrap?: ")
type = input()
print("Which filling would you like (1-6)?: ")
filling = input()

#selection statements for sandwich options
if type == "sandwich":
    if filling == 1:
        total = total + 2.8
    elif filling == 2:
        total = total + 2.5
    elif filling == 3 or filling == 4:
        total = total + 2.10
    elif filling == 5:
        total = total + 2.90
    else:
        print("You have not entered a valid filling option")

#selection statements for wrap options


#ask user if they want crisps and add to order total


#ask user if they want a drink and add to order total 

print(f"The total of your order is £{total}")