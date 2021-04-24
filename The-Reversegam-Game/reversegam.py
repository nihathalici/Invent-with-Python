# Reversegam: a clone of Othello/Reversi
import random
import sys

WIDTH = 8 # Board is 8 spaces wide.
HEIGHT = 8 # Board is 8 spaces tall

def drawBoard(board):
    # Print the board passed to this function. Return None.
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s]' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    # Create a brand-new, blank board data structure.
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # Return False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, return a list of spaces that would become
    # the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # First step in the x direction
        y += ydirection # First step in the y direction
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction.
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse
                # direction until we reach the original space, noting
                # all the tiles along the way.
            while True:
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    # Return True if the coordinates are located on the board.
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):
    # Return a new board with periods marking the valid moves the player can make.
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    # Return a list of [x, y] lists of valid moves for the given player on the given board.
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    pass

def enterPlayerTile():
    pass

def whoGoesFirst():
    pass

def makeMove(board, tile, xstart, ystart):
    pass

def getBoardCopy(board):
    pass

def isOnCorner(x, y):
    pass

def getPlayerMove(board, playerTile):
    pass

def getComputerMove(board, computerTile):
    pass

def printScore(board, playerTile, computerTile):
    pass

def playGame(playerTile, computerTile):
    pass
