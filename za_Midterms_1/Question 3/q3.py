import sys
import time
sys.setrecursionlimit(99999)

lengths = list(map(int,input().split()))
target = int(input())
numTiles = 0

memo = [-1] * (target + 1)

def minTile(L):

    minTiles = sys.maxsize
    
    if L <= 0:
        return 0
    
    # Check for memoization
    if memo[L] != -1:
        return memo[L]
    
    # Main logic
    else:
        for length in lengths:
            remaining = L - length
            # print(f"length {length}, remaining {remaining}")
            if remaining >= 0:
                numTiles = minTile(remaining) + 1
                if numTiles < minTiles:
                    minTiles = numTiles
    
        # Record memoization
        memo[L] = minTiles

        return(minTiles)
    
# Dynamic Programming
for i in range(target, -1, -1):
    (minTile(i))
print (memo[target])

# for i in range(target):
#     minTile(i)
# print(memo[target])










# for i in range(target, -1, -1):
#     minTile(i)