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
    print(f"Correct guesses = {correct_guesses}")
    print("Enter X1: ")
    x1 = int(input())
    print("Enter Y1: ")
    y1 = int(input())
    symbol1 = hidden_board[y1][x1]
    print(f"Symbol is: {symbol1}")
    print("Enter X2: ")
    x2 = int(input())
    print("Enter Y2: ")
    y2 = int(input())
    symbol2 = hidden_board[y2][x2]
    print(f"Symbol is: {symbol2}")
    if hidden_board[y1][x1] == hidden_board[y2][x2]:
        print("CORRECT! You found a match!")
        correct_guesses = correct_guesses + 1
        user_board[y1][x1] = hidden_board[y2][x2]
        user_board[y2][x2] = hidden_board[y2][x2]
    else:
        print(" Not a match!")
print("Amazing work - you found all the pairs of symbols")