#board of 8 pairs of symbols they have to find
hidden_board = [
    ["A","B","H","G"],
    ["F","A","C","F"],
    ["E","B","G","H"],
    ["E","D","C","D"],
]
# blank board that gets shown to user
user_board = [
    [" "," "," "," "],
    [" "," "," "," "],
    [" "," "," "," "],
    [" "," "," "," "],
]
#helper subroutine function to print out 2D board neatly
def print_board(board):
    print("  | 0 | 1 | 2 | 3 |")
    board_row = 0
    for row in board:
        new_row = str(board_row)
        for col in row:
            new_row = new_row + " | " + col
        print(new_row + " |")
        board_row = board_row + 1
# start main program loop
print("**** Welcome to the Pairs Match Game ****")
print("There are eight pairs of symbols hidden in this grid")
print("Enter the X and Y coordinates for two symbols (0-3)")
correct_guesses = 0
while correct_guesses < 8:
    print_board(user_board)
    # Ask user for the X and Y position for symbol 1
    # store symbol1 in a variable
    # Ask user for the X and Y position for symbol 2
    # store symbol2 in a variable
    # Check if symbol1 is the same as symbol2
    # If so print out "Congratulations you have found a match"
    # ... and add one the the correct guess count.
    # ...and update the user_board show the position of the 2 matched symbols on user board.
    # Else print out "No match"

print("Amazing work - you found all the pairs of symbols")
