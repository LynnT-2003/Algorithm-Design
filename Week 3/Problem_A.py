coins = list(map(int, input().split()))
change = int(input())
calls = 0

def mincoin(v, coins):
    global calls
    minCoins = float('inf')
    if v == 0:
        return 0
    
    for coin in coins:
        remaining = v - coin
        if remaining >= 0:
            numCoins = mincoin(remaining, coins) + 1
            calls += 1
            if numCoins < minCoins:
                minCoins = numCoins
    print(calls)
    return minCoins

result = mincoin(change, coins)
print(result)
