
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
n = 8 # number of columns - A, B, C ...
m = 8 # number of rows - 1, 2, 3 ...

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
    n = size_n
    m = size_m
    global board
    global first_player
    board = [[0 for x in range (n)] for x in range (m)]
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
    if (dir == HORIZONTAL and y>=7):
        return False
    if (dir == VERTICAL and x>=7):
        return False
    if (dir == VERTICAL):
        if board[y][x] == 0 and board[y+1][x] == 0:
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
    if (next%2 == 0):
        x_won = True
        for x in range (n-1):
            for y in range (m):
                if board[y][x] == 0 and board[y][x+1] == 0:
                    x_won = False
                    break
        if x_won:
            return 'X'
        
    # 'X' plays next, check VERTICAL    
    elif (next%2 == 1):
        o_won = True
        for x in range (n):
            for y in range (m-1):
                if board[y][x] == 0 and board[y+1][x] == 0:
                    o_won = False
                    break
        if o_won:
            return 'O'
    return 'N' # N -> No winner

def print_board():
    """
    The print_board function prints the current state of the game board.
    It takes no arguments and returns nothing.
    
    :return: A graphical representation of the game board
    """
    print("  ", end="")
    for i in range (n):
        print(chr(i+ord("A"))+" ", end="")
    
    print("\n ", "= "*n)

    for i in range (m, 0, -1):
        print(str(i)+"ǁ", end="")
        for j in range (n):
            field = board[m-i][j]
            # check if field is empty
            if (field == 0):
                print(" ", end="")
            elif (field%2 == 1):
                print("X", end="")
            elif (field%2 == 0):
                print("O", end="")
            print("|" if j < n-1 else "ǁ", end="")
        print(str(i))
        if (i != 1):
            print(" ", "- "*n)

    print(" ", "= "*n)
    print("  ", end="")
    for i in range (n):
        print(chr(i+ord("A"))+" ", end="")

initialize(8, 8, 1)
print_board()