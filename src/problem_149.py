# Problem 149: https://projecteuler.net/problem=149


def table():
    size = 4_000_000
    s = [0] * size

    for k in range(1, 56):
        s[k - 1] = (100003 - 200003 * k + 300007 * k**3) % 1_000_000 - 500_000

    for i in range(55, size):
        s[i] = (s[i - 24] + s[i - 55] + 1_000_000) % 1_000_000 - 500_000

    return s


def solve():
    n = 2000
    a = table()
    best = 0

    def scan(start, step, length):
        nonlocal best
        cur = 0
        i = start
        for _ in range(length):
            cur = max(0, cur + a[i])
            best = max(best, cur)
            i += step

    for r in range(n):
        scan(r * n, 1, n)
    for c in range(n):
        scan(c, n, n)

    for c in range(n):
        scan(c, n + 1, n - c)
        scan(c, n - 1, c + 1)
    for r in range(1, n):
        scan(r * n, n + 1, n - r)
        scan(r * n + n - 1, n - 1, n - r)

    return best


if __name__ == "__main__":
    print(solve())
