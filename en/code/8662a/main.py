chocolate_price = 10
crisps_price = 15
drink_price = 20

print("Choose an item:")
print("a: Chocolate bar", chocolate_price, "coins")
print("b: Crisps", crisps_price, "coins")
print("c: Drink", drink_price, "coins")

choice = input("Enter your choice: ")
if choice == 'a':
    print("The price of a chocolate bar is",chocolate_price, "coins.")
elif choice == 'b':
    print("The price of crisps is", crisps_price, "coins.")
elif choice == 'c':
    print("The price of a drink is", drink_price, "coins.")
else:
    print("Invalid choice!")