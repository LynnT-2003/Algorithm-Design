# Kadane's Algorithm

predicted_changes  = list(map(int, input().split()))

def max_profit(predicted_changes):
    n = len(predicted_changes)

    max_profit = predicted_changes[0]
    current_profit = predicted_changes[0]

    for i in range(1, n):
        current_profit = max(predicted_changes[i], current_profit + predicted_changes[i])
        max_profit = max(max_profit, current_profit)

    return max_profit

print(max_profit(predicted_changes)) 