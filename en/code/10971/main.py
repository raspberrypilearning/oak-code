#board of 8 pairs of symbols they have to find hidden_board





# blank board that gets shown to user user_board




#helper subroutine function to print out 2D board neatly
def print_board(board):
    for row in board:
        line = ""
        for col in row:
            line = line + " | " + col
        print(line + " |")
#call subroutine to print boards

