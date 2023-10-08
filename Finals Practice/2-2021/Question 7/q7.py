class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v/w


x = input().split()
N = int(x[1])
M = int(x[0])
item = []

for i in range(N):
    item.append(obj(*map(int, input().split())))

maxV = 0
count = 0


def Bound(i, sumW, sumV):
    global item, N, M

    RightWeight = 0
    SV = 0
    propotion = 1
    j = i + 1

    # proportion == 1 means the item[t] can be put into the knapsack physically
    # M-sumW-RightWeight > 0 means there is still space in the knapsack

    # t < N means there are still items to be considered
    while j < N and proportion == 1:
        # if the item[t] can be put into the knapsack physically then proportion is 1
        # otherwise proportion is the proportion of the item[t] that can be put into the knapsack

        proportion = min(M - sumW - RightWeight, item[j].w) / item[j].w
        RightWeight += proportion * item[j].w
        SV += proportion * item[j].v
        j += 1

    return SV + sumV


def dfs(i, sumW, sumV):
    global maxV, item, N, M, count

    count += 1
    if i == N:
        maxV = max(maxV, sumV)  # update maxV
    else:
        # only consider if it is possible to put item[h] into the knapsack
        if sumW + item[i].w <= M:
            newsumW = sumW + item[i].w
            dfs(i+1, newsumW, sumV+item[i].v)

        # Bound is the maximum possible value of the knapsack illegally
        # If you cheat and still cannot get a better solution, then there is no need to consider the rest of the items
        if Bound(i, sumW, sumV) > maxV:  # only consider if it is possible to get a better solution
            dfs(i+1, sumW, sumV)


item.sort(key=lambda x: x.r, reverse=True)
dfs(0, 0, 0)
print(maxV)

# Explanation:
# - The `dfs` function takes three arguments:
#   - `i` represents the index of the current item.
#   - `sumW` is the current total weight in the knapsack.
#   - `sumV` is the current total value in the knapsack.
# - `count` keeps track of the number of recursive calls.
# - `maxBound` stores the maximum achievable value estimated by the Bound function.

# Within the function:
# - It first calculates the upper bound (`maxBound`) based on the current state.
# - Then, it checks if we have reached the end of the item list (`i == N`).
#   - If so, it updates `maxV` with the maximum value found so far.
# - If we haven't reached the end of the item list:
#   - It explores two branches:
#     1. Takes the current item (if it fits within the knapsack's capacity) and recursively calls `dfs` with updated parameters.
#     2. Skips the current item if its inclusion doesn't exceed the upper bound, avoiding unnecessary exploration.

# This function uses pruning based on the upper bound (`maxBound`) to optimize the search, only exploring branches that have the potential to lead to better solutions, improving the efficiency of the Knapsack problem-solving algorithm.