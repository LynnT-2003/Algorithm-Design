coins = list(map(int, input().split()))
change = int(input())
counter = 0

def mincoin(v, coins):
    global counter
    counter += 1
    minCoins = float('inf')
    if v == 0:
        return 0
    
    for coin in coins:
        remaining = v - coin
        if remaining >= 0:
            numCoins = mincoin(remaining, coins) + 1
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

result = mincoin(change, coins)
print(f"{result}, {counter} calls")
