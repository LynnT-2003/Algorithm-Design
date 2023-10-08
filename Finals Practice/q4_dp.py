# Read input
h, w = map(int, input().split())
board = []
for _ in range(h):
    row = list(map(int, input().split()))
    board.append(row)

# Initialize a 2D table to store the maximum total token values
dp = [[0] * w for _ in range(h)]

# Initialize the first row of the dp table with the token values from the board
dp[0] = board[0]

# Iterate through each row from the second row to the last
for i in range(1, h):
    for j in range(w):
        # Calculate the maximum token value by considering three possible moves
        max_val = dp[i - 1][j]  # Move directly below
        if j > 0:
            max_val = max(max_val, dp[i - 1][j - 1])  # Move diagonally left
        if j < w - 1:
            max_val = max(max_val, dp[i - 1][j + 1])  # Move diagonally right

        # Add the current token value to the maximum value
        dp[i][j] = max_val + board[i][j]

# The maximum total token value is the maximum value in the last row of the dp table
max_total_token_value = max(dp[h - 1])

# Print the result
print(max_total_token_value)