import time

k = int(input())
li = list(map(int, input().split()))

def binary_search(li, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


start_time = time.process_time()

li.sort()
for i in range(len(li)):
    # note: we cannot use integer division here
    j = binary_search(li, k / li[i], i + 1, len(li) - 1) 
    if j != -1:
      print( [li[i], li[j]] )
      break

end_time = time.process_time()
running_time = end_time - start_time
print(f"Binary Search running time: {running_time}")
