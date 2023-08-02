import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

memo = [[-1 for _ in range(3)] for _ in range(L)]

def nWays(d, s):
    if d == L:
        if s == FLAT:
            return 1
        else:
            return 0
    else:
        if memo[d][s] != -1:  # Check if value already computed and stored in the memo list
            return memo[d][s] 
        
        counter = 0
        if s == FLAT:
            counter += nWays(d+1, UPPER2)
            counter += nWays(d+1, LOWER2)   # Actually, this is symmetric to UPPER2 
            if d < L-1:
                counter += nWays(d+2, FLAT)
        else:  # s is either UPPER2 or LOWER2
            counter += nWays(d+1,FLAT)
            if d < L-1:
                counter += nWays(d+2, s)
        
        # Store the computed value in the memo list before returning
        memo[d][s] = counter
        return counter

for i in range(L, -1, -1):
    for j in range(3):
        nWays(i, j)

print(memo[0][FLAT])


