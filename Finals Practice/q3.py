# A partitioning function, as that of quicksort, is provided. The partition will arrange
# the list A[p:r+1] into 3 parts; A[q], A[p:q], and A[q+1:r+1]. After partitioning, every value in A[p:q]
# is less than or equal to A[q], and every value in A[q+1:r+1] is more than A[q]. The function returns
# q, which is the index of the pivot.
# Write a Python 3 program that utilizes the given partition function to find the kth order statistic,
# which is the kth smallest value in the entire list.
# The program takes a sequence of numbers and a value of k as input and prints the kth order
# statistic as output.
# Hint Upon partitioning, decide based on the returned pivot index whether to recursively search

# Given the partition function
def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def kth_order_statistic(arr, p, r, k):
    if p < r:
        q = partition(arr, p, r)
        left_length = q - p + 1

        if k == left_length:
            return arr[q]
        elif k < left_length:
            return kth_order_statistic(arr, p, q - 1, k)
        else:
            return kth_order_statistic(arr, q + 1, r, k - left_length)
    else:
        return arr[p]

# Input: A line containing N integers, a sequence of numbers
arr = [2,8,3,7,4,6,5]
k = 4

# Find the kth order statistic
kth_statistic = kth_order_statistic(arr, 0, len(arr) - 1, 5)

# Output the result
print(kth_statistic)
