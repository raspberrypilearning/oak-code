def num_dogs():
   
   
   return total_dogs

def num_days():
   
   
   return total_days

def num_walks(total_dogs, total_days):
   
   
   return total_walks

def total_charge(total_walks):
   
   
   return total_cost

def invoice(total_dogs, total_days, total_walks, total_cost):


total_dogs = num_dogs()
total_days = num_days()
total_walks = num_walks(total_dogs,total_days)
total_cost = total_charge(total_walks)
invoice(total_dogs, total_days, total_walks, total_cost)
