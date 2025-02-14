chocolate_price = 10
crisps_price = 15
drink_price = 20
more_items = True

print("Choose an item:")
print(f"a: Chocolate bar {chocolate_price} coins")
print(f"b: Crisps {crisps_price} coins")
print(f"c: Drink {drink_price} coins")

while more_items == True:
    print("Enter your choice: ")
    choice = input()
    if choice == "a":
        print(f"The price of a chocolate bar is {chocolate_price} coins.")
    elif choice == "b":
        print(f"The price of crisps is {crisps_price} coins.")
    elif choice == "c":
        print(f"The price of a drink is {drink_price} coins.")
    else:
        print("Invalid choice!")
    print("Do you want more items? (y/n) ")
    more = input()
    if more == "y":
        more_items = True
    else:
        more_items = False
print("Thank you for using the vending machine")