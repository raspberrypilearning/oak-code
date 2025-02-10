#This function adds two numbers
def add(x,y):
    return x + y

#This function subtracts two numbers
def subtract(x,y):
    return x - y

#This function multiplies two numbers
def multiply(x,y):
    return x * y

#This function divides two numbers
def divide(x,y):
    return x / y

#Display menu and take user input
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("--------------------------")
print("Enter choice(1/2/3/4): ")
choice = int(input())
print("Enter first number: ")
num1 = int(input())
print("Enter second number")
num2 = int(input())


#Selection statements to call functions and display result
if choice == 1:
    result = add(num1,num2)
    print(f"{num1} + {num2} = {result}")
elif choice == 2:
    result = subtract(num1,num2)
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    result = multiply(num1,num2)
    print(f"{num1} * {num2} = {result}")
else:
    result = divide(num1,num2)
    print(f"{num1} / {num2} = {result}")
    