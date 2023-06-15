import time

k = int(input())
li = list(map(int, input().split()))
start_time = time.process_time()

for i in range(len(li)):
  for j in range(i+1,len(li)):
    # print(li[i], li[j])
    if li[i]*li[j] == k:
      print([li[i], li[j]])
      break
    

end_time = time.process_time()
running_time = end_time - start_time
print(f"Running time: {running_time}")