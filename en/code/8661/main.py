distance_travelled = 0
treasure_found = False

while treasure_found == False:
    print("Keep going", distance_travelled, "steps travelled so far")
    print("How many steps do you want to go now?")
    steps = int(input())
    distance_travelled = distance_travelled + steps
# Code to check for the treasure goes here
print("Treasure found after", distance_travelled, "steps!")