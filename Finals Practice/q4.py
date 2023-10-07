def max_token_value(h, w, tokens):
    def dfs(row, col):
        if row < 0 or row >= h or col < 0 or col >= w:
            return 0
        
        current_token = tokens[row][col]
        tokens[row][col] = 0  # Mark the current square as visited
        
        below = dfs(row + 1, col)
        left = dfs(row + 1, col - 1)
        right = dfs(row + 1, col + 1)
        
        tokens[row][col] = current_token  # Restore the value of the current square
        
        return current_token + max(below, left, right)
    
    max_value = 0
    for col in range(w):
        max_value = max(max_value, dfs(0, col))
    
    return max_value

# Predefined sample input
h, w = 6, 5
tokens = [
    [6, 2, 5, 3, 1],
    [3, 1, 8, 4, 2],
    [2, 1, 3, 1, 1],
    [1, 2, 2, 1, 6],
    [2, 2, 1, 4, 3],
    [2, 1, 4, 5, 4]
]

# Calculate the maximum possible total token value
max_total_value = max_token_value(h, w, tokens)

# Output the result
print(max_total_value)
