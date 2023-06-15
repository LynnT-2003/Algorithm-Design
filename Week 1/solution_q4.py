li = list(map(int, input().split()))
accumulated_list = []

accumulated_list.append(li[0])
for i in range(1, len(li)):
    accumulated_list.append(sum(li[0:i])+li[i])

print(li)
print(accumulated_list)