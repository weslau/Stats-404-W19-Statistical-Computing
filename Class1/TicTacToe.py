import pdb
import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# print(theBoard)
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


random.seed(111)

# start over from scratch
'''
turn = 'X'
list freepositions = []
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    #find available positions
    positions = theBoard.values()
    for i in range(len(theBoard.values())):
        if theBoard.values[i] == ' ':
            freepositions.append(i)


    #pick an empty spot
    random.choice(freepositions)
    move = input()

    ##from class notes
    def get_empty_positions(board):
        #return set (key if value == ' ' else notempty for (key,value) in board
        return [key for (key,value) in board.items() if value == " "]

    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


printBoard(theBoard)
'''
#simulation algortihm
#person 1=X
#pick and empty spot
#place your x in that spot

#person 2=)
#pick an empty spot
#place a 0 in that spot

#function to see who goes first
def whoGoesFirst():
    # Randomly choose the X or O to go first
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return 'O'
#function to check if player has won
#inputs = player character (X or O) and the current state of theBoard. outputs = True if player won, else false
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # bo = board and le = character's letter
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or # across the top
    (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or # across the middle
    (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or # across the bottom
    (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or # down the left side
    (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or # down the middle
    (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or # down the right sid
    (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or # diagonal
    (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le)) # diagonal

#write function that checks for all open positions in myBoard and randomly returns the key of one
#input = theBoard. Output = a random key name (with the value of  ' ')
def checkOpenMoves(board):
    #filtered_board = {k:v for (k,v) in board.items() if ' ' in k}
    filtered_board = {}
    for key,val in board.items():
        if val == ' ':
            filtered_board.update({key: val})
    return filtered_board
#def chooseRandomMove (input = board, output = key of random open move)
def chooseRandMove (board):
    #select only open moves
    filteredB = checkOpenMoves(board)
    return random.choice(list(filteredB.keys()))

turn = whoGoesFirst()

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    #move = input()
    # insert code for picking (randomly) an open position on theBoard and changing the value to X
    move = chooseRandMove(checkOpenMoves(theBoard)) #key for the move
    theBoard[move] = turn
    # insert break condition check if turn won the game
    if isWinner(theBoard, turn) == True:
        printBoard(theBoard)
        print("the winner is " + turn)
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

#time to test out all the functions individually in python and run the whole code (or do that first)