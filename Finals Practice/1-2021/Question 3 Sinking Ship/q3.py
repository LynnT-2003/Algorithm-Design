from simplePriorityQueue import *
N = int(input())
House = []
for _ in range(N):
    House.append(list(map(int, input().split())))

class state:
    def __init__(self, i, j, g):
        self.i = i
        self.j = j
        self.g = g
        self.index = None

PQ = Simple_Priority_Queue(lambda x, y: x.g > y.g)
s = state(-1, -1, 0)
PQ.enqueue(s)
p = []
for i in range(N):
    u = PQ.dequeue()
    p.append(u)

    for v in House[i]:
        a = state(-1, -1, v)
        PQ.enqueue(a)

u = PQ.dequeue()
p.append(u)

print(sum(list(map(lambda a:a.g, p))))