chocolate_price = 10
crisps_price = 15
drink_price = 20
more_items = True

print("Choose an item:")
print("a: Chocolate bar", chocolate_price, "coins")
print("b: Crisps", crisps_price, "coins")
print("c: Drink", drink_price, "coins")

while more_items == True:
    choice = input("Enter your choice: ")

    if choice == "a":
        print("The price of a Chocolate bar is",chocolate_price, "coins.")
    elif choice == "b":
        print("The price of Crisps is", crisps_price, "coins.")
    elif choice == "c":
        print("The price of a Drink is", drink_price, "coins.")
    else:
        print("Invalid choice!")
    more = input("Do you want more items? (y/n) ")
    if more == "y":
        more_items = True
    else:
        more_items = False
print("Thank you for using the vending machine")