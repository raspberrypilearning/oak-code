a = 10
b = 15
c = 20
more_items = True
x = 0
print("Choose an item:")
print(f"a: Chocolate bar {a} coins")
print(f"b: Crisps {b} coins")
print(f"c: Drink {c} coins")
while more_items == True:
    print("Enter your choice: ")
    choice = input()
    if choice == "a":
        print(f"The price of a Chocolate bar is {a} coins.")
        x = x + a
    elif choice == "b":
        print(f"The price of Crisps is {b} coins.")
        x = x + b
    elif choice == "c":
        print(f"The price of a Drink is {c} coins.")
        x = x + c
    else:
        print("Invalid choice!")
    print("Do you want more items? (y/n) ")
    more = input()
    if more == "y":
        more_items = True
    else:
        more_items = False
print(f"The total price is: {x}")
print("Thank you for using the vending machine")