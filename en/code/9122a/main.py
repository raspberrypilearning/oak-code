from dice import dicerolls
attacker_points = 0
defender_points = 0
attacker = dicerolls(3)
defender = dicerolls(2)
print("Players’ rolls")
print(f"Attacker: {attacker}")
print(f"Defender: {defender}")
attacker.sort(reverse=True)
defender.sort(reverse=True)
print("Sorted")
print(f"Attacker: {attacker}")
print(f"Defender: {defender}")
if attacker[0] > defender[0]:
    defender_points = defender_points - 1
    attacker_points = attacker_points + 1
else:
    attacker_points = attacker_points - 1
    defender_points = defender_points + 1
if attacker[1] > defender[1]:
    defender_points = defender_points - 1
    attacker_points = attacker_points + 1
else:
    attacker_points = attacker_points - 1
    defender_points = defender_points + 1
print(f"Attacker points: {attacker_points}")
print(f"Defender points: {defender_points}")
