# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

# TODOs:
# 1. Find all TODO items and see whether you can improve the code.
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random


def drawBoard(board):
    """This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0)"""
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    """Lets the player type which letter they want to be.
       Returns a list with the player’s letter as the first item, 
       and the computer's letter as the second."""
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()

    # first element => the player’s letter, second element => the computer's letter.
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def whoGoesFirst():
    """Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def playAgain():
    """This function returns True if the player wants to play again, otherwise it returns False."""
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def makeMove(board, letter, move):
    """Insert input letter into the board."""
    board[move] = letter


def isWinner(bo, le):
    """Given a board and a player’s letter, 
    this function returns True if that player has won.

    We use bo instead of board and le instead of letter 
    so we don’t have to type as much."""

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            # across the middle    # TODO: Fix the indentation of this lines and the following ones.
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    dupeBoard = []

    for i in range(0, len(board)):  # TODO: Clean this mess!
        dupeBoard.append(board[i])

    return dupeBoard


def isSpaceFree(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '


def getPlayerMove(board):
    """Let the player type in their move."""
    move = ' '  # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:  # TODO: How would you write this pythanically? (You can google for it!)
        return random.choice(possibleMoves)
    else:  # TODO: is this 'else' necessary?
        return None


# TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
def getComputerMove(board, computerLetter):
    """Given a board and the computer's letter, determine where to move and return that move."""
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:  # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    """Return True if every space on the board has been taken. 
    Otherwise return False."""
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def play():
    """Main controller for the game loop."""

    def shouldContinue(board, letter):
        """Determines whether to continue the game or not."""
        if isWinner(board, letter) or isBoardFull(board):
            return False
        return True

    def playerMove():
        """The logic that takes care of the player's turn."""
        move = getPlayerMove(board)
        makeMove(board, playerLetter, move)

        continueOn = shouldContinue(board, playerLetter)
        if not continueOn:
            drawBoard(board)

        if isWinner(board, playerLetter):
            print("Hooray! You have won the game!")
        elif isBoardFull(board):
            print("The game is a tie!")

        return continueOn

    def computerMove():
        """The logic that takes care of the computer's turn."""
        move = getComputerMove(board, computerLetter)
        makeMove(board, computerLetter, move)

        continueOn = shouldContinue(board, computerLetter)
        if not continueOn:
            drawBoard(board)

        if isWinner(board, computerLetter):
            print("The computer has beaten you! You lose :(")
        elif isBoardFull(board):
            print("The game is a tie!")

        return continueOn

    def playRound(curr):
        """Controls logic for one round of Tic Tac Toe."""
        while curr != "stop":
            if curr == "player":
                drawBoard(board)
                move = playerMove()
                curr = "computer" if move is True else "stop"
            elif curr == "computer":
                move = computerMove()
                curr = "player" if move is True else "stop"

    print('Welcome to Tic Tac Toe!')

    while True:
        board = [" " for block in range(TOTAL_BOXES + 1)]
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')

        playRound(turn)

        if not playAgain():
            break


if __name__ == "__main__":
    # parameters for the board
    BOARD_LENGTH = 3
    TOTAL_BOXES = BOARD_LENGTH**2

    play()
