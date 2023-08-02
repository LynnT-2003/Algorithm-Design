import sys
import time
sys.setrecursionlimit(10000)

lengths = list(map(int,input().split()))
target = int(input())
numTiles = 0

memo = [-1] * (target + 1)

def minTile(v):

    minTiles = sys.maxsize
    
    if v <= 0:
        return 0
    
    # Check if the result is already memoized
    if memo[v] != -1:
        return memo[v]
    
    else:
        for length in lengths:
            remaining = v - length
            # print(f"length {length}, remaining {remaining}")
            if remaining >= 0:
                numTiles = minTile(remaining) + 1
                if numTiles < minTiles:
                    minTiles = numTiles
    
        # Memoize the result
        memo[v] = minTiles

        return(minTiles)
    
# Use a loop to populate the memo list
for i in range(target, -1, -1):
    minTile(i)

print(minTile(target))