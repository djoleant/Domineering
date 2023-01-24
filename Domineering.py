
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Domineering                                                              │
  │ Authors:                                                                 │
  │     Emilija Ćojbašić, 18026                                              │
  │     Matija Špeletić, 18043                                               │
  │     Đorđe Antić, 17544                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 """

# Imports:
from cmath import sqrt

# Constants:
HORIZONTAL = 0
VERTICAL = 1

HUMAN = 0
COMPUTER = 1

# Global variables:
first_player = HUMAN
board = [[]]
asym_move = None
next = 1
n = 8  # number of columns - A, B, C ...
m = 8  # number of rows - 1, 2, 3 ...
asym_percent_floor=62
asym_percent_ceil=63

safe_moves_coef = 10


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
            for y in range(1, m):
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


def get_valid_moves(board):
    """
    The get_valid_moves function takes in a board and returns all valid moves.
    A move is represented by a tuple of the form (y, x, orientation), where y is the row number and x is the column number. 
    Orientation can either be 0 or 1 to indicate whether it's horizontal or vertical respectively.
    
    :param board: Pass the current state of the board
    :return: A list of tuples
    """
    valid_moves = []
    if (next % 2 == 0):
        for x in range(n-1):
            for y in range(m):
                # board[y][x] == 0 and board[y][x+1] == 0:
                # is_valid(x, y, HORIZONTAL):
                if board[y][x] == 0 and board[y][x+1] == 0:
                    valid_moves.append(
                        ((y, x, HORIZONTAL), make_move(y, x, HORIZONTAL)))
                    # break

    elif (next % 2 == 1):

        for x in range(n):
            for y in range(1, m):
                # board[y][x] == 0 and board[y-1][x] == 0:
                # is_valid(x, y, VERTICAL):
                if board[y][x] == 0 and board[y-1][x] == 0:
                    valid_moves.append(
                        ((y, x, VERTICAL), make_move(y, x, VERTICAL)))
                    # break

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
    """
    The heuristic function returns a score that is the sum of:
    - The difference in the number of available moves between the current player and its opponent.
    - The difference in the number of safe moves for each piece, computed only for squares where there are pieces from both players. 
        - A safe move is a move to an empty square that doesn't result in your own piece being flipped (i.e., it's not suicidal). 
        - If you're playing as Player 1, this means you want to maximize this count since it corresponds to pieces with odd parity; otherwise, you want to minimize it since even parity corresponds
    
    :param state: Determine the current state of the game
    :param move: Store the move that was made by the opponent
    :return: The following values:
    """
    global safe_moves_coef, asym_percent_floor, asym_percent_ceil
    # number of remaining horizontal moves
    horizontal = 0
    for x in range(n-1):
        for y in range(m):
            if state[y][x] == 0 and state[y][x+1] == 0:
                horizontal += 1

    # number of remaining vertical moves
    vertical = 0
    for x in range(n):
        for y in range(1, m):
            if state[y][x] == 0 and state[y-1][x] == 0:
                vertical += 1

    # give priority to center
    center_x, center_o, empty = 0, 0, 0
    # for x in range(n//4, 3*n//4):
    #     for y in range(m//4, 3*m//4):
    #         if state[y][x] == 0:
    #             empty += 1
    #         elif state[y][x] % 2 == 1:
    #             center_x += 1
    #         elif state[y][x] % 2 == 0:
    #             center_o += 1
    # if first_player == COMPUTER:
    #     if center_x >= 8:
    #         center_x, center_o, empty = 0, 0, 0
    # else:
    #     if center_o >= 8:
    #         center_x, center_o, empty = 0, 0, 0

    safe_moves_c, safe_moves_h = 0, 0
    if first_player == COMPUTER:
        for x in range(n):
            for y in range(m-1):
                if state[y][x] == 0 and state[y+1][x] == 0\
                        and (x == 0 or (state[y][x-1] != 0 and state[y+1][x-1] != 0)) and \
                        (x == n-1 or (state[y][x+1] != 0 and state[y+1][x+1] != 0)):
                    safe_moves_c += 1

    else:
        for y in range(m):
            for x in range(n-1):
                if state[y][x] == 0 and state[y][x+1] == 0\
                        and (y == 0 or (state[y-1][x] != 0 and state[y-1][x+1] != 0)) and \
                        (y == n-1 or (state[y+1][x] != 0 and state[y+1][x+1] != 0)):
                    safe_moves_h += 1

    empty = 0
    for x in range(n):
        for y in range(m):
            if state[y][x] == 0:
                empty += 1
    asym = 0
    coef = (empty+2)*100.0/(m*n)
    if coef > asym_percent_floor and coef < asym_percent_ceil:
        # safe_moves_coef=0
        if move[2] == HORIZONTAL:
            if move[1] % 2 == 0:
                asym = 1
                #print(coef, asym, move)
        else:
            if move[0] % 2 == 0:
                asym = 1

    dist = 0
    if asym_move != None:
        if move[2] == asym_move[2]:  # isti pravac
            dist = ((move[1]-asym_move[1])**2+(move[0]-asym_move[0])**2)**0.5
            if dist > 0.95 and dist < 1.05:
                dist = 10

    return (horizontal-vertical)+safe_moves_h*safe_moves_coef+n*(m-1)+m*(n-1) if first_player == HUMAN else \
        (vertical-horizontal)+n*(m-1)+m*(n-1)+safe_moves_c*safe_moves_coef + asym*30 - dist*7


def max_value(state, depth, alpha, beta, move):
    """
    The max_value function is a recursive function that takes in the current state, 
    the depth of the search tree, alpha and beta values. It returns a tuple containing 
    the best move to take for the player at this turn (represented by its column number), 
    and its corresponding heuristic value. The max_value function first checks if it has reached 
    its desired depth or if there are no more moves left to make in which case it will return a tuple with:
    (None, None) as both elements. If neither of these cases apply then it will call min_value on each possible move from
    the
    
    :param state: Keep track of the current state
    :param depth: Limit the depth of your search
    :param alpha: Keep track of the best score we have found so far along with its corresponding move
    :param beta: Prune the search tree
    :param move: Keep track of the last move made
    :return: The best move for the player to move
    """
    next_states = get_valid_moves(state)
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
    """
    The min_value function is a helper function for the max_value function. It 
    takes in a state, depth, alpha and beta values as input. The min_value function 
    iterates through all of the possible moves that can be made from the given state.  
    If there are no more moves to make or if we have reached our maximum depth then it 
    returns an (state, heuristic) tuple with its heuristic value being equal to what 
    the heuristic returns for that particular state and move combination. Otherwise it  
    calls itself recursively on each of the next states until one of
    
    :param state: Represent the current state of the game
    :param depth: Limit the depth of the search
    :param alpha: Keep track of the best score we have found so far along with the corresponding move
    :param beta: Keep track of the best score that the maximizing player can currently achieve
    :param move: Keep track of the move that was made to get from the parent node to this node
    :return: The minimum value of the next state and its move
    """
    next_states = get_valid_moves(state)
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
    """
    The minmax function takes a state, the depth of the search tree, whether it is my move or not (True for me and False for opponent), 
    the alpha value to use in pruning, beta value to use in pruning and finally a best_move tuple that will be set if there is one. 
    The function then checks if we have reached our desired depth limit or if the game has ended. If so it returns an evaluation of the board. 
    If not it calls either max_value or min_value depending on whether I am moving or not.
    
    :param state: Keep track of the current state of the game
    :param depth: Limit the depth of the search
    :param my_move: Determine whether the current node is a max or min node
    :param alpha: Keep track of the best score we have found so far along the path to state
    :param beta: Keep track of the best score that the maximizing player can currently achieve
    :return: A tuple of the form (value, move) where value is the value of that state for me and move is a possible next move
    """
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
    global board, next, first_player, asym_move
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
            move = next_state[2]
            if move[2] == HORIZONTAL:
                if move[1] % 2 == 0:
                    asym_move = move
                #print(coef, asym, move)
            else:
                if move[0] % 2 == 0:
                    asym_move = move
            next += 1
        print_board()
        win = check_winner()
        if win != "N":
            print("\n")
            print("Winner is " + win)
            break
        on_move = HUMAN if on_move == COMPUTER else COMPUTER


if __name__ == "__main__":
    play_game(8, 8, first=COMPUTER)
