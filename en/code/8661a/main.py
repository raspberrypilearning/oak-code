distance_travelled = 0
treasure_found = False

while treasure_found == False:
    print(f"Keep going {distance_travelled} steps travelled so far")
    print("How many steps do you want to go now?")
    steps = int(input())
    distance_travelled = distance_travelled + steps
# Code to check for the treasure goes here
    if distance_travelled >= 250:
      treasure_found = True
print(f"Treasure found after {distance_travelled} steps!")