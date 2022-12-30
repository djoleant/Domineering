
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Domineering                                                              │
  │ Authors:                                                                 │
  │     Emilija Ćojbašić, 18026                                              │
  │     Matija Špeletić, 18043                                               │
  │     Đorđe Antić, 17544                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 """

# Constants:
HORIZONTAL = 0
VERTICAL = 1

HUMAN = 0
COMPUTER = 1

# Global variables:
first_player = HUMAN
board = [[]]
next = 1
n = 8  # number of columns - A, B, C ...
m = 8  # number of rows - 1, 2, 3 ...


def initialize(size_n, size_m, first):
    """
    The initialize function sets up the board for a new game. 
    It takes two integers, size_n and size_m, as arguments. 
    The function then creates a board of n rows by m columns and fills it with zeros.

    :param size_n: Set the number of columns in the board
    :param size_m: Set the number of rows in the board
    :param first: Set the first player
    :return: The values of n and m
    """
    global n
    global m
    n = size_n
    m = size_m
    global board
    global first_player
    board = [[0 for x in range(n)] for x in range(m)]
    first_player = first

# x -> row number
# y -> column letter


def is_valid(x, y, dir):
    """
    The is_valid function checks if a move is valid. It takes in the x and y coordinates of the piece to be moved,
    as well as the direction (VERTICAL or HORIZONTAL) that it will be moving. If it is a valid move, then True
    is returned; otherwise False is returned.

    :param x: Determine the x coordinate of the selected position
    :param y: Determine the y coordinate of the selected position
    :param dir: Determine whether the function is being called to check if a block can be placed horizontally or vertically
    :return: True if the move is valid
    """
    if (dir == HORIZONTAL and x >= n-1):
        return False
    if (dir == VERTICAL and y < 1):
        return False
    if (dir == VERTICAL):
        if board[y][x] == 0 and board[y-1][x] == 0:
            return True
    elif (dir == HORIZONTAL):
        if board[y][x] == 0 and board[y][x+1] == 0:
            return True

    return False


def check_winner():
    """
    The check_winner function checks if the game has been won by either player.
    It does this by checking each row, column and diagonal for a sequence of two
    identical characters (0s in proper direction). If no winner is found, it returns 'N'.
    If X wins, it returns 'X', and if O wins it returns 'O'.

    :return: 'X' if 'X' wins, 'O' if 'O' wins and 'N' otherwise
    """
    # 'O' plays next, check HORIZONTAL
    if (next % 2 == 0):
        x_won = True
        for x in range(n-1):
            for y in range(m):
                if board[y][x] == 0 and board[y][x+1] == 0:
                    x_won = False
                    break
        if x_won:
            return 'X'

    # 'X' plays next, check VERTICAL
    elif (next % 2 == 1):
        o_won = True
        for x in range(n):
            for y in range(1,m):
                if board[y][x] == 0 and board[y-1][x] == 0:
                    o_won = False
                    break
        if o_won:
            return 'O'
    return 'N'  # N -> No winner


def play_move(x, y):
    """
    The play_move function takes two arguments, x and y, which are the coordinates of the move.
    It then checks if that move is valid or not. If it is valid, it places a tile on that spot.

    :param x: Specify the x coordinate of the move
    :param y: Specify the y coordinate of the move
    :return: Nothing
    """
    global next
    dir = VERTICAL if next % 2 == 1 else HORIZONTAL
    if not is_valid(x, y, dir):
        print("Invalid move")
        return False

    if dir == HORIZONTAL:
        board[y][x] = next
        board[y][x+1] = next

    elif dir == VERTICAL:
        board[y][x] = next
        board[y-1][x] = next

    next += 1
    # check_winner()
    return True


def get_valid_moves():
    """
    The get_valid_moves function returns a list of valid moves for the current player.
    The function takes no arguments and returns a list of tuples, where each tuple contains 
    the coordinates (y,x) and the type of move (HORIZONTAL or VERTICAL).

    :return: A list of tuples that represent the valid moves in the current state
    """
    valid_moves = []
    if (next % 2 == 0):
        for x in range(n-1):
            for y in range(m):
                # board[y][x] == 0 and board[y][x+1] == 0:
                if board[y][x] == 0 and board[y][x+1] == 0:#is_valid(x, y, HORIZONTAL):
                    valid_moves.append(
                        ((y, x, HORIZONTAL), make_move(y, x, HORIZONTAL)))
                    #break

    elif (next % 2 == 1):

        for x in range(n):
            for y in range(1,m):
                # board[y][x] == 0 and board[y-1][x] == 0:
                if board[y][x] == 0 and board[y-1][x] == 0:#is_valid(x, y, VERTICAL):
                    valid_moves.append(
                        ((y, x, VERTICAL), make_move(y, x, VERTICAL)))
                    #break

    return valid_moves


def make_move(y, x, dir):
    """
    The make_move function takes three arguments: x, y, and dir. 
    The function will create a new board by copying the old one
    and make the move.

    :param x: Indicate the x coordinate of the current position
    :param y: Indicate the row of the board
    :param dir: Determine whether the move is horizontal or vertical
    :return: A new board with the move made
    """
    global board, next
    new_board = [row[:] for row in board]
    if dir == HORIZONTAL:
        new_board[y][x] = new_board[y][x+1] = next
        # next+=1
    elif dir == VERTICAL:
        new_board[y][x] = new_board[y-1][x] = next
        # next+=1
    return new_board


def print_board():
    """
    The print_board function prints the current state of the game board.
    It takes no arguments and returns nothing.

    :return: A graphical representation of the game board
    """
    print("  ", end="")
    for i in range(n):
        print(chr(i+ord("A"))+" ", end="")

    print("\n ", "= "*n)

    for i in range(m, 0, -1):
        print(str(i)+"ǁ", end="")
        for j in range(n):
            field = board[m-i][j]
            # check if field is empty
            if (field == 0):
                print(" ", end="")
            elif (field % 2 == 1):
                print("X", end="")
            elif (field % 2 == 0):
                print("O", end="")
            print("|" if j < n-1 else "ǁ", end="")
        print(str(i))
        if (i != 1):
            print(" ", "- "*n)

    print(" ", "= "*n)
    print("  ", end="")
    for i in range(n):
        print(chr(i+ord("A"))+" ", end="")

    print()


def heuristic(state, move):
    #global first_player
    # number of remaining horizontal moves
    horizontal = 0
    for x in range(n-1):
        for y in range(m):
            if state[y][x] == 0 and state[y][x+1] == 0:
                horizontal += 1

    # number of remaining vertical moves
    vertical = 0
    for x in range(n):
        for y in range(1,m):
            if state[y][x] == 0 and state[y-1][x] == 0:
                vertical += 1
    
    # give priority to center
    center_x,center_o,empty=0,0,0
    for x in range(n//4,3*n//4):
        for y in range(m//4,3*m//4):
            if state[y][x]==0:
                empty+=1
            elif state[y][x]%2==1:
                center_x+=1
            elif state[y][x]%2==0:
                center_o+=1
    if first_player==COMPUTER:
        if center_x>=8:
            center_x,center_o,empty=0,0,0
    else:
        if center_o>=8:
            center_x,center_o,empty=0,0,0

    safe_moves_c,safe_moves_h=0,0
    if first_player==COMPUTER:
        for x in range(n):
            for y in range(m-1):
                if state[y][x] == 0 and state[y+1][x] == 0\
                    and (x==0 or (state[y][x-1]!=0 and state[y+1][x-1]!=0)) and \
                    (x==n-1 or (state[y][x+1]!=0 and state[y+1][x+1]!=0)):
                        safe_moves_c+=1
    
    else:
        for y in range(m):
            for x in range(n-1):
                if state[y][x] == 0 and state[y][x+1] == 0\
                    and (y==0 or (state[y-1][x]!=0 and state[y-1][x+1]!=0)) and \
                    (y==n-1 or (state[y+1][x]!=0 and state[y+1][x+1]!=0)):
                        safe_moves_h+=1
    
    return horizontal-vertical+safe_moves_h+n*(m-1)+m*(n-1)+(center_o-center_x)*0.5 if first_player==HUMAN else \
        vertical-horizontal+n*(m-1)+m*(n-1)+safe_moves_c+(center_x-center_o)*0.5


def max_value(state, depth, alpha, beta, move):
    next_states = get_valid_moves()
    # print(next_states)
    if depth == 0 or next_states is None or len(next_states) == 0:
        return (state, heuristic(state, move), move)
    else:
        for s in next_states:
            alpha = max(alpha,
                        min_value(s[1], depth - 1, alpha, beta, s[0]),
                        key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha


def min_value(state, depth, alpha, beta, move):
    next_states = get_valid_moves()
    if depth == 0 or next_states is None or len(next_states) == 0:
        return (state, heuristic(state, move), move)
    else:
        for s in next_states:
            beta = min(beta,
                       max_value(s[1], depth - 1, alpha, beta, s[0]),
                       key=lambda x: x[1])
        if beta[1] <= alpha[1]:
            return alpha
    return beta


def minmax(state, depth, my_move, alpha=(board, -1, None), beta=(board, 10000000, None)):
    if my_move:
        return max_value(state, depth, alpha, beta, None)
    else:
        return min_value(state, depth, alpha, beta, None)


def play_game(size_n, size_m, first):
    """
    The play_game function plays a game of Domineering.
    It takes three arguments: size_n, size_m and first.
    size_n is the number of rows in the board, while size_m is the number of columns in it.
    first specifies which player moves first - either HUMAN or COMPUTER. 

    :param size_n: Set the number of columns in the board
    :param size_m: Set the number of rows in the board
    :param first: Specifies which player makes the first move
    """
    global board, next, first_player
    initialize(size_n, size_m, first)
    on_move = first_player
    print_board()
    while True:
        if on_move == HUMAN:
            x_y = input()
            y = int(x_y[0])
            x = ord(x_y[2].upper())-ord("A")
            y = m - y
            if not play_move(x, y):
                continue
        elif on_move == COMPUTER:
            next_state = minmax(board, 3, True)
            print(next_state)
            board = next_state[0]
            next += 1
        print_board()
        win = check_winner()
        if win != "N":
            print("\n")
            print("Winner is " + win)
            break
        on_move = HUMAN if on_move == COMPUTER else COMPUTER


if __name__ == "__main__":
    # TODO: Implement min-max move making logic
    play_game(8, 8, first=HUMAN)
