li = list(map(int, input().split()))

def Sum(x,i,j):
    s = 0
    for k in range(i,j+1):
        s +=  x[k]
    return(s)

def find_max_subsequence_sum(li):
    n = len(li)
    max_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            current_sum = Sum(li, i, j)
            max_sum = max(max_sum, current_sum)

    return max_sum

result = find_max_subsequence_sum(li)
print("The sum of the maximum subsequence is:", result)
