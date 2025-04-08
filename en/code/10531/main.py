times_table = int(input("Enter the number for the times table"))
answer = 0
print(f"Here is the {times_table} times table")
for calc in range(1,11):
    answer = calc * times_table
    print(f"{calc} times {times_table} is {answer}")
