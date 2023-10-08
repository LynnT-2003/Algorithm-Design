import heapq
packets = list(map(int, input().split()))\

def minimumCost(packets):
  total_cost = 0
  heapq.heapify(packets)
  while len(packets) > 1:
    min1 = heapq.heappop(packets)
    min2 = heapq.heappop(packets)
    heapq.heappush(packets, min1 + min2)
    total_cost += min1 + min2
  return total_cost

print(minimumCost(packets))