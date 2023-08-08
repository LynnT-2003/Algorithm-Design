import sys

data = list(map(int, input().split()))
N = len(data)

x = [None for _ in range(N)]
min_diff = sys.maxsize
total_sum = sum(data)

# Initialize memoization table with -1
memo = [[-1 for _ in range(total_sum+1)] for _ in range(N+1)]

def Combination(i, group1_sum):
    global min_diff, x, N, memo

    if memo[i][group1_sum] != -1:
        return memo[i][group1_sum]

    if i == N:
        group2_sum = total_sum - group1_sum
        diff = abs(group1_sum - group2_sum)
        if diff < min_diff:
            min_diff = diff
        return 1
    else:
        x[i] = 0
        v = Combination(i+1, group1_sum + data[i])
        x[i] = 1
        v += Combination(i+1, group1_sum)
        memo[i][group1_sum] = v  # Store the result in memoization table
        return v

# for i in range(N+1):
#     for j in range(total_sum+1):
#         Combination(i, j)

Combination(0, 0)

print(min_diff)
