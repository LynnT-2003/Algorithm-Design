import time
import sys
sys.setrecursionlimit(10000)

data = list(map(int, input().split()))
print(data)
N = len(data)
x = [None for _ in range(N)]
min_diff = sys.maxsize  # Initialize the minimum difference to a large value

def BalanceSplit(i):
    global x, N, data, min_diff

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
        return

    else:
        x[i] = 0
        BalanceSplit(i + 1)
        x[i] = 1
        BalanceSplit(i + 1)

st = time.process_time()
BalanceSplit(0)
et = time.process_time()

print(f"Minimum difference between two groups: {min_diff}")
print(f"Running Time: {et - st}")
