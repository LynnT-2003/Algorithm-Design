prices = list(map(int, input().split()))
n = len(prices)
total = 0
counter = 0

calls = [0] * (n+1)
memo = [None] * (n+1)

maximumRevenue = float('-inf')

def maxRev(l):
    global total
    global counter
    global calls
    global memo
    global maximumRevenue

    if memo[l] is not None:
        return memo[l]

    if l == 0:
        return 0
    
    for i in range(1, l+1):
        remaining = l - i
        total = prices[i-1] + maxRev(remaining)
        maximumRevenue = max(maximumRevenue, total)
    memo[l] = maximumRevenue
    
    counter += 1    
    calls[l] += 1
    return maximumRevenue

print(f"Maximum Revenue: {maxRev(n)}, {counter} calls")
print("Number of calls for each maxRev():", calls[1:])
