from random import choice
from time import sleep

# display the menu to the user

def menu():
    print("Welcome to battle boats")
    print("Would you like to\n1. Play a game\n2. Resume a game\n3. Read instructions\n4. Quit")
    answer = input()
    if answer == "1":
        play() # start the game
    elif answer == "2":
        resume() # resume a game
    elif answer == "3":
        instructions() # view the instructions

# displays the grid for the player based on where they are in game play

def display_grid(grid):
    print(" ", grid[0][0], "│", grid[0][1], "│", grid[0][2], "│", grid[0][3], "│", grid[0][4], "│", grid[0][5], "│", grid[0][6], "│", grid[0][7], "│", grid[0][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[1][0], "│", grid[1][1], "│", grid[1][2], "│", grid[1][3], "│", grid[1][4], "│", grid[1][5], "│", grid[1][6], "│", grid[1][7], "│", grid[1][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[2][0], "│", grid[2][1], "│", grid[2][2], "│", grid[2][3], "│", grid[2][4], "│", grid[2][5], "│", grid[2][6], "│", grid[2][7], "│", grid[2][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[3][0], "│", grid[3][1], "│", grid[3][2], "│", grid[3][3], "│", grid[3][4], "│", grid[3][5], "│", grid[3][6], "│", grid[3][7], "│", grid[3][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[4][0], "│", grid[4][1], "│", grid[4][2], "│", grid[4][3], "│", grid[4][4], "│", grid[4][5], "│", grid[4][6], "│", grid[4][7], "│", grid[4][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[5][0], "│", grid[5][1], "│", grid[5][2], "│", grid[5][3], "│", grid[5][4], "│", grid[5][5], "│", grid[5][6], "│", grid[5][7], "│", grid[5][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[6][0], "│", grid[6][1], "│", grid[6][2], "│", grid[6][3], "│", grid[6][4], "│", grid[6][5], "│", grid[6][6], "│", grid[6][7], "│", grid[6][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[7][0], "│", grid[7][1], "│", grid[7][2], "│", grid[7][3], "│", grid[7][4], "│", grid[7][5], "│", grid[7][6], "│", grid[7][7], "│", grid[7][8])
    print(" ───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" ", grid[8][0], "│", grid[8][1], "│", grid[8][2], "│", grid[8][3], "│", grid[8][4], "│", grid[8][5], "│", grid[8][6], "│", grid[8][7], "│", grid[8][8])

# allow the player to add their boats to their fleet

def add_boats(fleet_grid):
    print("------------PLAYER FLEET-------------")
    display_grid(fleet_grid)
    print("Build your fleet by entering coordinates for each boat")
    boats = 0
    adding_boats = boats < 5
    while adding_boats: # add boats until there are 5
        print("Enter battle boat coordinates e.g. A1:")
        coordinates = input()
        coordinates = grid_location(coordinates)
        row = coordinates[0]
        column = coordinates[1]
        if fleet_grid[row][column] == "B":
            print("Occupied!")
        else:
            fleet_grid[row][column] = "B"
            print("------------PLAYER FLEET-------------")
            display_grid(fleet_grid)
            boats += 1
        adding_boats = boats < 5
    return fleet_grid

def play():

    # create a blank player grid

    fleet_grid = [["F", "A", "B", "C", "D", "E", "F", "G", "H"],
                  ["1", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["2", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["3", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["4", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["5", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["6", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["7", " ", " ", " ", " ", " ", " ", " ", " "],
                  ["8", " ", " ", " ", " ", " ", " ", " ", " "]]

    # add boats to the fleet grid

    add_boats(fleet_grid)

    # create the opponent fleet locations

    opponent = computer_fleet()
    print(opponent) # not required for actual game!

    target_grid = target_tracker()

    player_casualties = 0
    computer_casualties = 0
    player_moves = []
    computer_moves = []

    turn = "player"

    # start the game

    while player_casualties < 5 and computer_casualties <5:

        if turn == "player":

            # player takes a turn

            print("-----------TARGET TRACKER------------")
            display_grid(target_grid)
            print("Get ready to fire!...")
            sleep(1)
            print("Enter target coordinates e.g. A1")
            target_coordinates = input()
            while target_coordinates in player_moves:
                print("Target already used, enter another coordinate:")
                target_coordinates = input()
            if target_coordinates in opponent:
                print("HIT!")
                computer_casualties += 1
                outcome = "H"
                opponent.remove(target_coordinates)
            else:
                print("MISS!")
                outcome = "M"
            player_moves.append(target_coordinates)
            target_coordinates = grid_location(target_coordinates)
            row = target_coordinates[0]
            column = target_coordinates[1]
            target_grid[row][column] = outcome
            print("-----------TARGET TRACKER------------")
            display_grid(target_grid)

            sleep(1)

            turn = "computer"

        elif turn == "computer":

            # computer takes a turn

            print("Computer takes aim...")
            sleep(2)
            computer_target = computer_hit()
            while computer_target in computer_moves:
                computer_target = computer_hit()
            print(computer_target)

            sleep(1)

            computer_moves.append(computer_target)

            computer_target = grid_location(computer_target)
            row = computer_target[0]
            column = computer_target[1]
            if fleet_grid[row][column] == "B":
                print("HIT!")
                player_casualties += 1
                fleet_grid[row][column] = "H"
            else:
                print("MISS!")

            sleep(1)

            print("------------PLAYER FLEET-------------")
            display_grid(fleet_grid)

            sleep(2)

            turn = "player"

    if player_casualties == 5:
        print("COMPUTER WINS!")
    else:
        print("YOU WIN!")


def grid_location(coordinates): # calculates the 2D list location based on given coordinates
    if coordinates[0] == "A":
        column = 1
    elif coordinates[0] == "B":
        column = 2
    elif coordinates[0] == "C":
        column = 3
    elif coordinates[0] == "D":
        column = 4
    elif coordinates[0] == "E":
        column = 5
    elif coordinates[0] == "F":
        column = 6
    elif coordinates[0] == "G":
        column = 7
    elif coordinates[0] == "H":
        column = 8
    if coordinates[1] == "1":
        row = 1
    elif coordinates[1] == "2":
        row = 2
    elif coordinates[1] == "3":
        row = 3
    elif coordinates[1] == "4":
        row = 4
    elif coordinates[1] == "5":
        row = 5
    elif coordinates[1] == "6":
        row = 6
    elif coordinates[1] == "7":
        row = 7
    elif coordinates[1] == "8":
        row = 8

    row_column = [row, column]
    return row_column


def computer_hit(): # randomly selects a coordinate for the computer to fire at
    columns = ["A", "B", "C", "D", "E", "F" ,"G" , "H"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
    column = choice(columns)
    row = choice(rows)
    coordinate = column + row
    return coordinate

def computer_fleet(): # randomly selects the location for the computer's fleet
    fleet = []
    columns = ["A", "B", "C", "D", "E", "F" ,"G" , "H"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
    boats = 0
    while boats < 5:
        column = choice(columns)
        row = choice(rows)
        coordinate = column + row
        if coordinate not in fleet:
            fleet.append(coordinate)
            boats += 1
    return fleet

def target_tracker(): # tracks the hits and misses on the computer's fleet
    target_grid = [["T", "A", "B", "C", "D", "E", "F", "G", "H"],
                   ["1", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["2", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["3", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["4", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["5", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["6", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["7", " ", " ", " ", " ", " ", " ", " ", " "],
                   ["8", " ", " ", " ", " ", " ", " ", " ", " "]]
    return target_grid

def resume():
    print("This will resume")

def instructions():
    print("~~~INSTRUCTIONS~~~")
    print("You and your opponent have a fleet of five boats")
    print("The aim of the game is to sink all five of your opponent's boats before they sink yours!")
    print("Take it in turns to enter coordinates and try and hit a target!")
    print("Press enter to return to the menu")
    input()
    menu()

menu()
