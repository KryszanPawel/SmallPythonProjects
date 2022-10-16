import numpy as np


def create_grid(n):
    """function create chessboard size n x n"""
    grid = []
    for row in range(n):
        grid.append([])
        for col in range(n):
            grid[row].append(0)
    return grid


def is_valid(Y, X):
    """function checks if position of queen is valid"""
    global chess
    if 1 in chess[Y]: # checks if row is clean, if not returns false
        return False
    column = [chess[i][X] for i in range(size)]
    if 1 in column:  # checks if column is clean, if not returns false
        return False
    for posx in range(size):  # checks if diagonals are clean, if not returns false
        for posy in range(size):
            if chess[posy][posx] == 1:
                if posy - Y == posx - X or posy - Y == - (posx - X):
                    return False
    return True # if all clear returns true


def is_solved():
    """function checks if puzzle is solved yet"""
    sum = 0
    global chess, size
    for row in range(size): # sums all number of queens in chessboard
        for col in range(size):
            sum += chess[row][col]
    if sum == size: #if amount of queens on board equals size of board returns true
        return True
    return False


def solve(col):
    """solver looks for queen position for indicated column """
    global chess, size
    if is_solved(): #checks if puzzle is solved yet, if yes terminates solver, if not lets solver work
        return True
    for row in range(size): #check every row in column for valid queen position
        if chess[row][col] == 0 and is_valid(row, col):
            chess[row][col] = 1 #puts the queen in first valid position
            if solve(col + 1): #try to solve puzzle for next column
                return True     #if returns true, mean puzzle is solved
            chess[row][col] = 0 #if not, position is not valid, checks next valid position
    return False


if __name__ == "__main__":
    size = int(input("How big chessboard do you want to solve? "))
    chess = create_grid(size)
    if solve(0):
        print(np.matrix(chess))
    else:
        print("No solution found")
