distance_traveled = 0
treasure_found = False

while treasure_found == False:
    print("Keep going", distance_traveled, "steps travelled so far")
    print("How many steps do you want to go now?")
    steps = int(input())
    distance_traveled = distance_traveled + steps
# Code to check for the treasure goes here
print("Treasure found after", distance_traveled, "steps!")