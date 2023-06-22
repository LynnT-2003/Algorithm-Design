import sys
sys.setrecursionlimit(10000)
n = 4
k = 2
x = [None] * n
count = 0

def comb(i, ones):
    global count
    if i == n:
        if ones == k:
            print(x) 
            count += 1
    else:
        x[i] = 0  # Option: not selected
        comb(i+1, ones)
        x[i] = 1  # Option: selected
        comb(i+1, ones + 1)

comb(0, 0)
print("Number of combinations with exactly", k, "ones:", count)