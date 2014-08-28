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
print ("\t~~~~~////////BATTLESHIP!////////~~~~~\n")
turns = eval(input("How many turns would you like to take?\n"))
board_size = eval(input("What should be the board size?\n"))
cls

#initializing board to all O's
#board = [["O" for x in range(board_size)][for y in range(board_size)]]
board =[]
for x in range(5):
    board.append(["O"] * 5)



def print_board(board):
    #function to display board clearly
    for row in board:
        print((" ".join(row)))

#display initial state
print_board(board)

#placing a ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
#debug
print (ship_row)
print (ship_col)

#simple if else cases
for turn in range(turns):
    cls
    print(("Turn #" + str(turn+1)))
    guess_row = int(eval(input("\n\n\tGuess Row:   ")))
    guess_col = int(eval(input("\n\n\tGuess Col:   ")))
    if guess_row == ship_row and guess_col == ship_col:
        print ("\n\n\tCongratulations! You sunk my battleship!")
        break
    elif turn <turns:
        if (guess_row < 0 or guess_row > board_size) or (guess_col < 0 or guess_col > board_size):
            print ("\n\n\tOops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("\n\n\tYou guessed that one already.")
            
        else:
            print ("\n\n\tYou missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == turns-1 :
            print ("\n\n\tGame Over")
            board[ship_row][ship_col] = "S"
            print ("\n\n\tDagnabbit! The ship was hiding here >")
        print_board(board)
