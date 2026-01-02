"""
You are given an m x n matrix board containing letters 'X' and 'O',
capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect
the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place
within the original board. You do not need to return anything.
"""


def solve(board):
    rows = len(board)
    cols = len(board[0])

    def dfs_capture(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
            return
        board[r][c] = "#"
        dfs_capture(r + 1, c)
        dfs_capture(r - 1, c)
        dfs_capture(r, c + 1)
        dfs_capture(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                dfs_capture(r, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "#":
                board[r][c] = "O"

    return board


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

print(solve(board))
