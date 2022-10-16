This is my interpretation of sudoku solver project.
Solver base of recursion with backtracking method.
Solver looks for first unsigned space in grid, than checks for first, possible valid number and insert it to the grid.
After that it starts over with next free space, until no number is valid.
In that case solver returns to last possible step and tries with next valid number.
Solver works this way until grid is solved properly.
