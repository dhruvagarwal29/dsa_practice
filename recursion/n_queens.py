#


def nQueens(n):
    result = []
    # creating n * n board filled with .
    board = [["." for i in range(n)] for j in range(n)]

    # taking 3 sets to check if queen is present in them or not
    col_set = set()
    pos_diagonal = set()  # [row + col] this is the right to left diagonal
    neg_diagonal = set()  # [row - col] this is the left to right diagonal

    def backtrack(row):

        # base condition
        if row == n:
            result.append(
                ["".join(r) for r in board]
            )  # add every row as a string in the result
            return

        for col in range(n):
            if (
                col in col_set
                or (row + col) in pos_diagonal
                or (row - col) in neg_diagonal
            ):
                continue

            col_set.add(col)
            pos_diagonal.add(row + col)
            neg_diagonal.add(row - col)
            board[row][col] = "Q"  # make this position as Q

            backtrack(row + 1)

            col_set.remove(col)
            pos_diagonal.remove(row + col)
            neg_diagonal.remove(row - col)
            board[row][col] = "."

    backtrack(0)
    return result


print(nQueens(4))
