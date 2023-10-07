# In a packet switched network, a message is broken into N message packets of different lengths.
# Eventually they need to be combined into one message for the complete delivery. However, only
# two packets can be combined at a time, and the cost to combining two packets is equal to sum of
# their lengths.

import heapq

packets = [4, 3, 2, 6]

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