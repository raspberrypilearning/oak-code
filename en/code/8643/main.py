print("Please enter your age: ")
age = int(input())
ticket_price = 0
if age < 3:
    print("You get in for free!") 
elif age < 12:  
    print("Is it peak season? (yes/no): ")
    is_peak_season = input()
    if is_peak_season == "yes":
        ticket_price = 25
    else: 
        ticket_price = 20
# Add code below to complete the task

print("Ticket price: £", ticket_price)