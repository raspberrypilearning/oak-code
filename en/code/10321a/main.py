print("---Welcome to Split My Pizza---")
print("How many slices does the Pizza have?")
slices_total = int(input())
print("How many people are sharing?")
people = int(input())

slices_each = slices_total//people
slices_remaining = slices_total%people

print(f"There are {slices_each} slices each")
print(f"There will be {slices_remaining} slices remaining")