import time 
start = time.process_time()

li = list(map(int, input().split()))

def kadane_algorithm(A):
    max_global = max_current = A[0]
    for i in range(1, len(A)):
        max_current = max(A[i], max_current + A[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

result = kadane_algorithm(li)
print("The sum of the maximum subsequence is:", result)

finish = time.process_time()
print("Running time: ", finish-start, " seconds")