N, T, R = map(int, input().split())
Sat = list(map(int, input().split()))
Sun = list(map(int, input().split()))
Sat.sort()
Sun.sort(reverse=True)
extra = 0
for i in range(N):
    overWork = Sat[i] + Sun[i] - T
    if overWork > 0:
        extra += overWork * R

print(extra)