import sys
sys.setrecursionlimit(10000)
n = 4
k = 3
x = [None] * n

def comb(i):
    if i == n:
        print(x)
        return 1
    else:
        x[i] = 0  # Option: not selected
        total = comb(i+1)
        x[i] = 1  # Option: selected
        total += comb(i+1)
        return total

print(comb(0))
