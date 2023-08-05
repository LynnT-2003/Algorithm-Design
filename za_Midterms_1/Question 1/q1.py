predicted_changes  = list(map(int, input().split()))

def max_profit(predicted_changes):
    n = len(predicted_changes)

    # Initialize variables to keep track of the maximum profit and current profit
    max_profit = predicted_changes[0]
    current_profit = predicted_changes[0]

    # Loop through the predicted changes to find the maximum sum subarray
    for i in range(1, n):
        current_profit = max(predicted_changes[i], current_profit + predicted_changes[i])
        max_profit = max(max_profit, current_profit)

    return max_profit

<<<<<<< HEAD
print(max_profit(predicted_changes)) 
=======
# Example usage:
print(max_profit(predicted_changes))  # Output: 12

>>>>>>> 15c68257fbbd80777df0646f6b1e62dbb88ec2e2
