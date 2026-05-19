# Problem 237: https://projecteuler.net/problem=237
MOD = 100_000_000
N = 10**12


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % MOD for j in range(n)] for i in range(n)]


def matpow(a, e):
    n = len(a)
    r = [[int(i == j) for j in range(n)] for i in range(n)]
    while e:
        if e % 2:
            r = matmul(r, a)
        a = matmul(a, a)
        e //= 2
    return r


def tours(n):
    base = [1, 1, 4, 8]
    if n <= 4:
        return base[n - 1]

    a = [
        [2, 2, -2, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]
    p = matpow(a, n - 4)
    v = [8, 4, 1, 1]
    return sum(p[0][i] * v[i] for i in range(4)) % MOD


def solve():
    return tours(N)


if __name__ == "__main__":
    print(solve())
