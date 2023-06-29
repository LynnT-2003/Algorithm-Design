prices = list(map(int, input().split()))
n = len(prices)
total = 0

def oneTime(l):
    print("Cutting one time:")
    for i in range(1, l):
        print(f"{i} & {l-i}: {prices[i-1]} + {prices[l-i-1]} = {prices[i-1] + prices[l-i-1]}")

def maxRev(l):
    global total
    maximumRevenue = float('-inf')
    if l == 0:
        return 0
    for i in range(1, l+1):
        remaining = l - i
        total = prices[i-1] + maxRev(remaining)
        if total > maximumRevenue:
            maximumRevenue = total
    return maximumRevenue

oneTime(n)
print(f"Maximum Revenue: {maxRev(n)}")
