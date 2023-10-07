import time

# Input
N = int(input("Enter the number of activities: "))
Activities = []
print("Enter activity details (start_time finish_time):")
for _ in range(N):
    start, finish = map(int, input().split())
    Activities.append((start, finish))


def ActivitySelection(n,Activities):
    # Sort Finish Time in Ascending Order
    Activities.sort(key=lambda x: x[1])

    #Always Select First Activity
    count = 1
    left = 0
    for right in range(1, n):
        # Activities are not back to back consecutive
        if Activities[left][1] < Activities[right][0]:
            print(Activities[left], Activities[right])
            count += 1
            left = right
    print(count)

st = time.process_time()
ActivitySelection(N, Activities)
et = time.process_time()
print(f"Running Time: {et-st}")