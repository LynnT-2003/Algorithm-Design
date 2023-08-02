import sys
import time
sys.setrecursionlimit(10000)

coins = list(map(int,input().split()))
target = int(input())
numCoins = 0
count = 0

def minCoin(v):

    minCoins = sys.maxsize
    
    if v <= 0:
        return 0
    
    else:
        for coin in coins:
            remaining = v - coin
            # print(f"coin {coin}, remaining {remaining}")
            if remaining >= 0:
                numCoins = minCoin(remaining) + 1
                if numCoins < minCoins:
                    minCoins = numCoins
        return(minCoins)

print(minCoin(target))