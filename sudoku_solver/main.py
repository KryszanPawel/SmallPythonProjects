import numpy


I = 0 # number of steps


def is_valid(grid, row, col, n):
    # if n in row return false
    if n in grid[row]:
        return False
    # if n  in col return false
    column = [grid[i][col] for i in range(9)]
    if n in column:
        return False

    # if n in sub-grid return false
    sub = []
    for x in range((col // 3) * 3, (col // 3) * 3 + 3):
        for y in range((row // 3) * 3, (row // 3) * 3 + 3):
            sub.append(grid[y][x])
    if n in sub:
        return False
    # else return true
    return True


def solve():
    global I, grid
    I += 1
    for row in range(9):  # for every row
        for col in range(9):  # and every column
            if grid[row][col] == 0:  # find blanc space
                for n in range(1, 10):  # check if n
                    if is_valid(grid, row, col, n):  # is valid number
                        grid[row][col] = n  # if yes try n
                        solve()  # go to next blanc space .... if no n is valid inside recurtion
                        grid[row][col] = 0  # put 0 back in a place and  goes back to for loop (n)
                return #if no valid n returns up in recursion
    print(numpy.matrix(grid))
    print(f"solved in {I} steps")



if __name__ == "__main__":
    grid = [                # sudoku grid to solve
        [0, 0, 0, 4, 0, 0, 0, 3, 0],
        [1, 0, 7, 0, 8, 0, 0, 0, 2],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 5],
        [5, 0, 9, 0, 0, 3, 0, 2, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 0],
        [9, 0, 2, 0, 7, 0, 0, 0, 1],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 7, 0, 0]
    ]

    solve()

