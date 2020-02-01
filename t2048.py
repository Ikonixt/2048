# Checks whether a given board has any
# possible move left. If no more moves,
# return True. Otherwise return False.
def isGameOver(board):
    if doKeyUp(board)[0] == False and doKeyDown(board)[0] == False and doKeyLeft(board)[0] == False and \
            doKeyRight(board)[0] == False:
        return True
    return False


def process(board, starty, endy, diry, startx, endx, dirx, isy, startedge, mody, modx):
    # Step 1: Move
    for rounds in range(len(board)):
        for y in range(starty, endy, diry):
            for x in range(startx, endx, dirx):
                if isy == True:
                    if y != startedge and board[y][x] != " " and board[y + mody][x + modx] == " ":
                        board[y + mody][x + modx] = board[y][x]
                        board[y][x] = " "
                else:
                    if x != startedge and board[y][x] != " " and board[y + mody][x + modx] == " ":
                        board[y + mody][x + modx] = board[y][x]
                        board[y][x] = " "

    # Step 2: Compact
    for y in range(starty, endy, diry):
        for x in range(startx, endx, dirx):
            if isy == True:
                if y != startedge and board[y][x] != " " and board[y][x] == board[y + mody][x + modx]:
                    number = int(board[y][x]) * 2
                    board[y + mody][x + modx] = str(number)
                    board[y][x] = " "
            else:
                if x != startedge and board[y][x] != " " and board[y][x] == board[y + mody][x + modx]:
                    number = int(board[y][x]) * 2
                    board[y + mody][x + modx] = str(number)
                    board[y][x] = " "

    # Step 3: Move2 electric bogaloo
    for rounds in range(len(board)):
        for y in range(starty, endy, diry):
            for x in range(startx, endx, dirx):
                if isy == True:
                    if y != startedge and board[y][x] != " " and board[y + mody][x + modx] == " ":
                        board[y + mody][x + modx] = board[y][x]
                        board[y][x] = " "
                else:
                    if x != startedge and board[y][x] != " " and board[y + mody][x + modx] == " ":
                        board[y + mody][x + modx] = board[y][x]
                        board[y][x] = " "

    return board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              pressems the 'Up' key.
def doKeyUp(board):
    temp = []
    for stuff in board:
        temp.append(stuff[:])

    board = process(board, 0, len(board), 1, 0, len(board[0]), 1, True, 0, -1, 0)

    if board == temp:
        return False, board
    if (len(emptyPos(board)) == 0):
        return False, board

    return True, board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.
def doKeyDown(board):
    temp = []
    for stuff in board:
        temp.append(stuff[:])

    board = process(board, len(board) - 1, -1, -1, 0, len(board[0]), 1, True, len(board) - 1, 1, 0)

    if board == temp:
        return False, board
    if (len(emptyPos(board)) == 0):
        return False, board

    return True, board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.
def doKeyLeft(board):
    temp = []
    for stuff in board:
        temp.append(stuff[:])

    board = process(board, 0, len(board), 1, 0, len(board[0]), 1, False, 0, 0, -1)

    if board == temp:
        return False, board
    if (len(emptyPos(board)) == 0):
        return False, board

    return True, board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.
def doKeyRight(board):
    temp = []
    for stuff in board:
        temp.append(stuff[:])

    board = process(board, 0, len(board), 1, len(board[0]) - 1, -1, -1, False, len(board[0]) - 1, 0, 1)

    if board == temp:
        return False, board
    if (len(emptyPos(board)) == 0):
        return False, board

    return True, board


# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board):
    lst = []
    row = len(board)
    col = len(board[0])
    for y in range(row):
        for x in range(col):
            if board[y][x] == ' ':
                coords = y, x
                lst.append(coords)

    return lst


# Returns a dictionary mapping each tile
# value on the board to its count (i.e.,
# how many times it appears on the board)
def hist(board):
    freqdic = {}
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != ' ':
                freqdic[int(board[y][x])] = freqdic.get(int(board[y][x]), 0) + 1

    return freqdic
