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
            return kth_order_statistic(arr, p, q-1, k)
        else:
            return kth_order_statistic(arr, q+1, r, k-left_length)
    else:
        return arr[p]
    
# def partition2(arr, left, right):
#     # Choose the pivot element
#     pivot = arr[right]
#     i = left - 1

#     # Partition the array into elements <= pivot and elements > pivot
#     for j in range(left, right):
#         if arr[j] <= pivot:
#             i += 1
#             # Swap elements arr[i] and arr[j]
#             arr[i], arr[j] = arr[j], arr[i]

#     # Place the pivot element in its correct position
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     return i + 1


# def kth_order_statistic2(arr, left, right, k):
#     if left == right:
#         # If the array has only one element, return it
#         return arr[left]

#     # Partition the array and get the pivot index
#     pivot_index = partition(arr, left, right)

#     if k == pivot_index:
#         # If k matches the pivot index, return the kth order statistic
#         return arr[pivot_index]
#     elif k < pivot_index:
#         # If k is less than the pivot index, search in the left subarray
#         return kth_order_statistic(arr, left, pivot_index - 1, k)
#     else:
#         # If k is greater than the pivot index, search in the right subarray
#         return kth_order_statistic(arr, pivot_index + 1, right, k)

    
# Input: Read the array and k
arr = list(map(int, input().split()))
k = int(input())

# Find kth order statistic
result = kth_order_statistic(arr, 0, len(arr) - 1, k)
# result2 = kth_order_statistic2(arr, 0, len(arr) - 1, k - 1)

# Output: Print the kth order statistic
print(result)
# print(result2)