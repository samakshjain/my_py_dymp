#for a random int
from random import randint

#for clearing screen
class cls(object):
    def __repr__(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        return ''

cls = cls()

#Welcome text + prompt
print "BATTLESHIP!"
turns = prompt("How many turns would you like to take?")
board_size = prompt("What should be the board size?")
cls

#initializing board to all O's
board = [["O" for x in range(board_size)][for y in range(board_size)]]


def print_board(board):
    #function to display board clearly
    for row in board:
        print " ".join(row)

#display initial state
print_board(board)

#placing a ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#debug
#ship_row = random_row(board)
#ship_col = random_col(board)
print ship_row
print ship_col

#simple if else cases
for turn in range(turns):
    cls
    print  "Turn #" + str(turn+1) 
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif turn <turns:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == turns-1 :
            print "Game Over"
            board[ship_row][ship_col] = "S"
            print "Dagnabbit! The ship was hiding here >"
            print_board(board)
        print_board(board)
