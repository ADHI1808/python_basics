def is_valid(board, row, col, n):
    # Check row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def n_queens_util(board, col, n, solutions):
    if col == n:
        solution = []
        for i in range(n):
            row = []
            for j in range(n):
                if board[i][j] == 1:
                    row.append('Q')
                else:
                    row.append('.')
            solution.append(''.join(row))
        solutions.append(solution)
        return

    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1
            n_queens_util(board, col + 1, n, solutions)
            board[i][col] = 0

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    n_queens_util(board, 0, n, solutions)
    return solutions

# Example usage
n = 4
solutions = n_queens(n)
print(f"Number of solutions for {n} queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)

