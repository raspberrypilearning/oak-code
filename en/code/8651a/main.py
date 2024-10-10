print("What is the passcode?")
passcode = int(input())
while passcode != 1234:
	print("Try again")
	passcode = input()
print("Phone unlocked!")