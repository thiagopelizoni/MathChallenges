# Problem 390: https://projecteuler.net/problem=390
from collections import deque


def solve(n=10**10):
    total = 0
    q = deque()
    b = 1
    while 8 * b**3 + b <= n:
        L = b
        D = 4 * L * L + 1
        u = 8 * L * L + 1
        v = 4 * L
        A, g = L, 0
        while True:
            A, g = u * A + D * v * g, v * A + u * g
            if A > n:
                break
            if g >= L:
                total += A
                q.append((A, L, g))
        b += 1
    while q:
        a, m, L = q.popleft()
        D = 4 * L * L + 1
        u = 8 * L * L + 1
        v = 4 * L
        for sy in (m, -m):
            A, g = a, sy
            while True:
                A, g = u * A + D * v * g, v * A + u * g
                if A > n:
                    break
                if g >= L:
                    total += A
                    q.append((A, L, g))
    return total


if __name__ == "__main__":
    print(solve())
