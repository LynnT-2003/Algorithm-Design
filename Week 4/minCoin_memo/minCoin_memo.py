import sys
sys.setrecursionlimit(1000000)

coins = list(map(int, input().split()))
v = int(input())
counter = 0
calls = [0] * (v+1)
memo = [None] * (v+1)
calls = [0] * (v+1)

def mincoin(v):
    global counter
    minCoins = float('inf')

    if memo[v] is not None:
        return memo[v]

    if v == 0:
        return 0
    
    for coin in coins:
        remaining = v - coin
        if remaining >= 0:
            numCoins = mincoin(remaining) + 1
            minCoins = min(minCoins, numCoins)
        memo[v] = minCoins
    
    counter += 1
    calls[v] += 1
    return minCoins

result = mincoin(v)
print(f"{result}, {counter} calls")
print("Number of calls for each minCoin():", calls[1:])
