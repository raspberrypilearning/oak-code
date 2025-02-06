def average_value(a, b, c):
    average = (a+b+c)/3
    average = round(average,2)
    print(f"The average value is {average}")

print(f"Enter the first number:")
num1 = int(input())
print(f"Enter the second number:")
num2 = int(input())
print(f"Enter the third number:")
num3 = int(input())

average_value(num1,num2,num3)