N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

calls = [0] * (N + 1)
counter = 0
memo = [[-1] * (M + 1) for i in range(N + 1)]

def maxVal(i, C):
    global counter
    if i == N:
        return 0
    
    if memo[i][C] != -1:
        return memo[i][C]
    
    calls[i] += 1
    
    skip = maxVal(i + 1, C)

    if w[i] <= C:
        take = v[i] + maxVal(i + 1, C - w[i])
    else:
        take = -1
    
    memo[i][C] = max(skip, take)

    counter += 1
    return memo[i][C]

print(maxVal(0, M))
print("Number of recursive calls:", counter)
