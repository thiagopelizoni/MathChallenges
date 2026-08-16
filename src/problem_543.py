# Problem 543: https://projecteuler.net/problem=543

from sympy import fibonacci, primepi


def count(n):
    ans = int(primepi(n))

    if n >= 4:
        ans += n // 2 + int(primepi(n - 2)) - 2

    m = n // 2
    if m >= 3:
        ans += (m - 2) * (n + 1) - m * (m + 1) + 6

    return ans


def solve():
    return sum(count(int(fibonacci(k))) for k in range(3, 45))


if __name__ == "__main__":
    print(solve())
