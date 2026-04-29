# Problem 148: https://projecteuler.net/problem=148


def count_rows(n):
    if n == 0:
        return 0

    p = 1
    block = 1
    while p * 7 <= n:
        p *= 7
        block *= 28

    q, r = divmod(n, p)
    return q * (q + 1) // 2 * block + (q + 1) * count_rows(r)


def solve():
    return count_rows(10**9)


if __name__ == "__main__":
    print(solve())
