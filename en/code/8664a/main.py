chocolate_price = 10
crisps_price = 15
drink_price = 20
more_items = True
total_price = 0

print("Choose an item:")
print("a: Chocolate bar", chocolate_price, "coins")
print("b: Crisps", crisps_price, "coins")
print("c: Drink", drink_price, "coins")

while more_items == True:
    print("Enter your choice: ")
    choice = input()
    if choice == "a":
        print("The price of a Chocolate bar is",chocolate_price, "coins.")
        total_price = total_price + chocolate_price
    elif choice == "b":
        print("The price of Crisps is", crisps_price, "coins.")
        total_price = total_price + crisps_price
    elif choice == "c":
        print("The price of a Drink is", drink_price, "coins.")
        total_price = total_price + drink_price
    else:
        print("Invalid choice!")
    print("Do you want more items? (y/n) ")
    more = input()
    if more == "y":
        more_items = True
    else:
        more_items = False
print("The total price is: ", total_price)
print("Thank you for using the vending machine")