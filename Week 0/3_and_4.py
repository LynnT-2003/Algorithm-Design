import time

k = int(input())
li = list(map(int, input().split()))
start_time = time.process_time()

DAT = {}
result_found = False

for num in li:
    DAT[num] = True
    key = k // num
    if k % num == 0 and DAT.get(key, False): #return False is key does not exist
        print([num, key])
        result_found = True
        break
# print(DAT)

if not result_found:
    print("No pair found")

end_time = time.process_time()
running_time = end_time - start_time
print(f"DAT Running time: {running_time}")
