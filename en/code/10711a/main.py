def num_dogs():
    print("Enter number of dogs: ")
    total_dogs = int(input())
    return total_dogs

def num_days():
    print("Enter number of days: ")
    total_days = int(input())
    return total_days

def num_walks(total_dogs, total_days):
    total_walks = total_dogs * total_days
    return total_walks

def total_charge(total_walks):
    total_cost = total_walks * 4.00
    return total_cost

def invoice(total_dogs, total_days, total_walks, total_cost):
    print(f"Number of dogs walked: {total_dogs}")
    print(f"Number of days walked: {total_days}")
    print(f"Total number of walks: {total_walks}")
    print(f"Total cost of invoice {total_cost}")

total_dogs = num_dogs()
total_days = num_days()
total_walks = num_walks(total_dogs,total_days)
total_cost = total_charge(total_walks)
invoice(total_dogs, total_days, total_walks, total_cost)
