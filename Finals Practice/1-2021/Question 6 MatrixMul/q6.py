MOD = 44711

def mat_mult(A, B):
    """Multiply matrix A and B modulo MOD."""
    n = len(A)
    m = len(A[0])
    p = len(B[0])

    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

# Computes matrix power using exponentiation by squaring
def mat_pow(m, n):
    if n == 1:
        return m


    half_pow = mat_pow(m, n // 2)
    if n % 2 == 0:
        return mat_mult(half_pow, half_pow)
    else:
        return mat_mult(mat_mult(half_pow, half_pow), m)

def tile(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = mat_pow([[4, -1], [1, 0]], (n-2) // 2)
        return (3* result[0][0] + result[0][1]) % MOD

print(tile(4999998))
print(tile(4999999998))