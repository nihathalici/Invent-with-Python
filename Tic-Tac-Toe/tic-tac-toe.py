import random

def drawBoard(board):
    ''' This function prints out the board that it was passed.
        "board" is a list of 10 strings representing the board
        (ignore index 0). '''
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    ''' Lets the player type which letter they want to be.
        Returns a list with the player's letter as the first
        item and the computer's letter as the second. '''
    letter = ''
    while not (letter == 'x' or letter == 'o'):
        print('Do you want to be x or o?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose which player goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    ''' Given a board and a player's ietter, this function returns
        True if that player has won.
        We use "bo" instead of "board" and "le" instead of "letter"
        so we don't have to type as much. '''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le) or # Diagonal

def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    pass


def getPlayerMove(board):
    pass


def choose RandomMoveFromList(board, movesList):
    pass


def getComputerMove(board, computerLetter):
    pass

def isBoardFull(board):
    pass
