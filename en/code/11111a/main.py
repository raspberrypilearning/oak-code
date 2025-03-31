players = []

add_players = True
while add_players:
    print("Enter a username:")
    username = input()
    print("Enter a password:")
    password = input()
    print("Enter a score")
    score = input()
    print("Enter highest score")
    highest_score = input()

    player = {"username" : username,
              "password" : password,
              "score" : score,
              "highest score": highest_score}

    players.append(player)

    print("Would you like to add another player? Y/N")
    answer = input().upper()
    if answer == "N":
        add_players = False

print(players)
print(players[0])
print("Which record would you like to print")
record_no = int(input())
print(players[record_no])