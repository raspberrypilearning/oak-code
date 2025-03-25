chocolate_price = 10
crisps_price = 15
drink_price = 20
more_items = True
total = 0

# menu for user to select items
print("Choose an item:")
print(f"a: Chocolate bar {chocolate_price} coins")
print(f"b: Crisps {crisps_price} coins")
print(f"c: Drink {drink_price} coins")

# while loop to continue until user does not want more items
while more_items == True:
    print("Enter your choice: ")
    choice = input()

    if choice == "a":
        print(f"The price of a Chocolate bar is {chocolate_price} coins.")
        total = total + chocolate_price
    elif choice == "b":
        print(f"The price of Crisps is {crisps_price} coins.")
        total = total + crisps_price
    elif choice == "c":
        print(f"The price of a Drink is {drink_price} coins.")
        total = total + drink_price
    else:
        print("Invalid choice!")

# ask user if they want more items
    print("Do you want more items? (y/n) ")
    more = input()
    if more == "y":
        more_items = True
    else:
        more_items = False

# display total price to user
print(f"The total price is: {total}")
print("Thank you for using the vending machine")