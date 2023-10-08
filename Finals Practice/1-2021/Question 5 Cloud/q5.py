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


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

def largest_cloud(matrix):
    rows, cols = M, N
    ds = DisjointSets(rows * cols)

    # For every cloud pixel, try to union it with its adjacent cloud pixels
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # up, down, left, right (adj)
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1: # valid
                        ds.union(i * cols + j, x * cols + y) # union the cloud pixels by their

    # Find the size of the largest cloud
    cloudcount = [0] * (rows * cols)
    for i in range(rows*cols):
        cloudcount[ds.findset(i)] += 1

    return max(cloudcount)

print(largest_cloud(matrix))