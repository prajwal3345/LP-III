# Design n-Queens matrix having first Queen placed. 
# Use backtracking to place remaining Queens to generate the final n-queen‘s matrix.


def solveNQueens(n: int, first_queen_col: int):
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"

    backtrack(1)  
    return res

if __name__ == "__main__":
    n = 8
    first_queen_col = 1
    board = solveNQueens(n, first_queen_col)[0]
    for row in board:
        print(" ".join(row))




# Defines the function solveNQueens which takes:
# n: the size of the board (n x n).
# first_queen_col: the fixed column position for the queen in the first row.
# These sets help track columns and diagonals where queens are placed:
# col: tracks columns where queens are already placed.
# posDiag (positive diagonals): tracks r + c, where r is the row and c is the column.
# negDiag (negative diagonals): tracks r - c, for left-leaning diagonals.
# res: List to store all valid board configurations.
# board: Initializes an n x n board filled with ".", representing empty spaces.
# Defines a helper function backtrack that places queens row by row.
# Checks if all queens have been placed (i.e., r == n). 
# If so, it adds the current board configuration to res as a list of strings.
# Loops over each column c in row r.
# Checks if column c, or the positive or negative diagonals (r + c) or (r - c) already have queens.
# If any constraint is violated, it skips to the next column.
# If no constraints are violated:
# Adds c to col, r + c to posDiag, and r - c to negDiag to mark those positions.
# Places a queen "Q" on board[r][c].
# Calls backtrack(r + 1) to place the next queen in the next row.
# After exploring with a queen in board[r][c], it removes the queen to backtrack:
# Removes c from col, r + c from posDiag, and r - c from negDiag.
# Resets board[r][c] to "." to try the next position in the loop.
# Manually places the first queen in the specified column first_queen_col in the first row.
# Updates col, posDiag, and negDiag to reflect this placement.
# Sets board[0][first_queen_col] = "Q" to place the queen on the board.
# Calls backtrack starting from row 1, as row 0 is already occupied by the first queen.
# Returns res, a list of all valid board configurations.
# Sets n = 8 for an 8x8 board and first_queen_col = 1 to fix the first queen in column 1 of the first row.
# Calls solveNQueens and selects the first valid solution from res to display.
# Prints the board row by row, showing "Q" for queens and "." for empty spaces.