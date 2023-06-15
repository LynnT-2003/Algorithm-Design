import time

k = int(input())
li = list(map(int, input().split()))

for i in range(len(li)):
  for j in range(i+1,len(li)):
    # print(li[i], li[j])
    if li[i]*li[j] == k:
      print([li[i], li[j]])
      break