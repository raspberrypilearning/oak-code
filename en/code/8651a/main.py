from random import randint 
rolls = 0
sixes = 0
while sixes < 10: 
  dice = randint(1,6)
  print(dice)
  if dice == 6:
    sixes = sixes + 1
  rolls = rolls + 1 
print("Ten sixes in", rolls, "dice rolls")