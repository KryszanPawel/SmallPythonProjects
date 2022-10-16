This is my interpretation of N_Queen problem solver project.
Solvers task is to find space for a queen in every column on chessboard.
The space must ensure queens safety. That means queens can't attack each other
by being in the same row, column and diagonal.
Solver base on recursion with backtracking.
Script looks for first valid position in column, starts over in next column, and so on, until no position in column is valid. In that case it goes back to last valid column and checks for next valid position.
Solver works until queen occupy spot in every column. In other case prints that there is no valid solution.

