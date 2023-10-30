import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution

def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    """
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (-1, -1), (-1, 1), (1, -1)
    ]
    for dx, dy in directions:
        r, c = row, col
        while 0 <= r < len(board) and 0 <= c < len(board):
            board[r][c] = "x"
            r += dx
            c += dy

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = [row[:] for row in board]
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be an integer greater than or equal to 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
    print(f"Found {len(solutions)} solutions")

    sys.exit(0)
