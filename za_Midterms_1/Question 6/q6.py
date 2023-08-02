import time
import sys
sys.setrecursionlimit(10000)

data = list(map(int, input().split()))
N = len(data)

x = [None for _ in range(N)]
min_diff = sys.maxsize  # Initialize the minimum difference to a large value

memo = [[-1 for _ in range(1 << N)] for _ in range(N+1)]

def BalanceSplit(i, mask):
    global x, N, data, min_diff

    if memo[i][mask] != -1:
        return memo[i][mask]

    if i == N:
        sum_group1 = 0
        sum_group2 = 0
        # Calculate the sum of each group based on the selected elements
        for j in range(N):
            if x[j]:
                sum_group1 += data[j]
            else:
                sum_group2 += data[j]
        # Calculate the difference between the sums of the two groups
        diff = abs(sum_group1 - sum_group2)
        # Update the minimum difference if the current difference is smaller
        min_diff = min(min_diff, diff)
        return diff

    else:
        x[i] = 0
        diff1 = BalanceSplit(i + 1, mask)
        
        x[i] = 1
        diff2 = BalanceSplit(i + 1, mask | (1 << i))

        # Memoize the result and return the minimum difference
        memo[i][mask] = min(diff1, diff2)
        return memo[i][mask]

# Use a loop to populate the memo list
for i in range(N+1):
    for j in range(1 << N):
        BalanceSplit(i, j)

# st = time.process_time()
# # BalanceSplit(0, 0)
# et = time.process_time()

print(f"Minimum difference between two groups: {min_diff}")
# print(f"Running Time: {et - st}")
