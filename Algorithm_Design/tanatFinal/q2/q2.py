import time

n = int(input())
M = []

# Read the input matrix
for _ in range(n):
    x = list(map(int, input().split()))
    M.append(x)

# Initialize a memoization table to store minimum path costs
dp = [[float('inf')] * n for _ in range(n)]

# Base case: The cost to move from a node to itself is 0
for i in range(n):
    dp[i][i] = 0
st = time.process_time()

# Dynamic programming to compute minimum path costs
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
et = time.process_time()

# Print the transformed matrix
for i in range(n):
    for j in range(n):
        if dp[i][j] == float('inf'):
            print(-1, end=' ')
        else:
            print(dp[i][j], end=' ')
    print()
print(et-st)
