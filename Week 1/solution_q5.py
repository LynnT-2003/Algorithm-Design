# import time 
# start = time.process_time()

li = list(map(int, input().split()))

def Sum(x, i, j):
    return sum(x[i:j+1])

# def find_max_subsequence_sum(li):
#     n = len(li)
#     max_sum = float('-inf')

#     for i in range(n):
#         for j in range(i, n):
#             current_sum = Sum(li, i, j)
#             print(f"compare: {max_sum}, {current_sum}")
#             max_sum = max(max_sum, current_sum)

#     return max_sum

# result = find_max_subsequence_sum(li)
# print("The sum of the maximum subsequence is:", result)

# finish = time.process_time()
# print("Running time: ", finish-start, " seconds")