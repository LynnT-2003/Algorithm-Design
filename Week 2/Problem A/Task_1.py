import sys
sys.setrecursionlimit(10000)

# li = list(map(int, input().split()))
# n = len(li)

n = 3
x = [None] * n

def comb(i):
    if i == n:
        print(x)
    else:
        x[i] = 0  # Option: not selected
        comb(i+1)
        x[i] = 1  # Option: selected
        comb(i+1)

comb(0)
