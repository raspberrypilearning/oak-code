age = int(input("Please enter your age: "))

ticket_price = 0
if age < 3:
    print("You get in for free!")
elif age < 12:  
    is_peak_season = input("Is it peak season? (yes/no): ")

    if is_peak_season == 'yes':
        ticket_price = 25
    else:
        ticket_price = 20
elif age >= 12:
    is_peak_season = input("Is it peak season? (yes/no): ")

    if is_peak_season == 'yes':
        ticket_price = 35
    else:
        ticket_price = 30

print("Ticket price: £", ticket_price)
    
