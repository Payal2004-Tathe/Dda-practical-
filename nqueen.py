def solveNQueens(n: int, first_queen_col: int):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
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

    # Place the first queen
    if 0 <= first_queen_col < n:
        col.add(first_queen_col)
        posDiag.add(0 + first_queen_col)
        negDiag.add(0 - first_queen_col)
        board[0][first_queen_col] = "Q"
        backtrack(1)
    else:
        print("Invalid column! It must be between 0 and", n - 1)
        return []

    return res


if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))
    first_queen_col = int(input(f"Enter column position (0 to {n - 1}) for the first queen: "))

    solutions = solveNQueens(n, first_queen_col)

    if not solutions:
        print("No solution found.")
    else:
        print(f"\nTotal Solutions Found: {len(solutions)}\n")
        for idx, board in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            for row in board:
                print(" ".join(row))
            print()
