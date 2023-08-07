def Fibonacci(n):
    a = [None for _ in range(n+2)]
    a[0], a[1] = 1, 1
    for i in range(2, n+2):
        a[i] = a[i-1] + a[i-2]

    print(a[n+1])

n = int(input())
Fibonacci(n)