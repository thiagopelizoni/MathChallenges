# Problem 316: https://projecteuler.net/problem=316


N = 10**16
LIM = 999_999


def g(n):
    s = str(n)
    total = 0

    for k in range(1, len(s) + 1):
        if s[:k] == s[-k:]:
            total += 10**k

    return total - len(s) + 1


def solve():
    return sum(g(N // n) for n in range(2, LIM + 1))


if __name__ == "__main__":
    print(solve())
