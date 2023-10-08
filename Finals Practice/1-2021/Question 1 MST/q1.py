class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n
        
    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u,v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

def Kruskal(V, Edges):
    Edges = sorted(Edges, key=lambda x: x[2])

    # Create Disjoint Set
    D = DisjointSets(V)

    W = 0
    edgecount = 0

    for u, v, w in Edges:
        if D.findset(u) != D.findset(v):
            D.union(u, v)
            W += w
            edgecount += 1

    print(W)

V, E = map(int, input().split())
Edges = [tuple(map(int, input().split())) for _ in range(E)]

# V, E = 4, 4
# Edges = [(0, 3, 15),
# (1, 2, 20),
# (1, 3, 24),
# (2, 3, 17)]

Kruskal(V, Edges)