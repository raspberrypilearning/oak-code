passcode = input("Enter the passcode to unlock") 
while passcode != "1978":
    print(f"{passcode} is incorrect")
    passcode = input("Enter the passcode to unlock")
print("Hello welcome to your phone")