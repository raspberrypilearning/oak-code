distance_traveled = 0
treasure_found = False

while treasure_found == False:
  print("Keep going", distance_traveled, "steps travelled")
  distance_traveled = distance_traveled + 10
  if distance_traveled >= 250:
    treasure_found = True
print("Treasure found after", distance_traveled, "steps!")