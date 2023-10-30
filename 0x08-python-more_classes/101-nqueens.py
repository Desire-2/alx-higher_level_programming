import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == "Q":
                solution.append([r, c])
    return solution

def xout(board, row, col):
    """X out spots on a chessboard where non-attacking queens cannot be placed."""
    n = len(board)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < n and 0 <= c < n:
            board[r][c] = "x"
            r, c = r + dr, c + dc

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for c in range(n):
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
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
    print(f"Found {len(solutions)} solutions")
