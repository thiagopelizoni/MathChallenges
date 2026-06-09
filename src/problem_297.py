# Problem 297: https://projecteuler.net/problem=297

from bisect import bisect_right


N = 10**17


def tables(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    acc = [0, 1]
    for i in range(2, len(fib)):
        acc.append(acc[i - 1] + acc[i - 2] + fib[i - 2])

    return fib, acc


def count(n):
    fib, acc = tables(n)
    ans = 0

    while n:
        i = bisect_right(fib, n - 1) - 1
        if i < 0:
            return ans

        r = n - fib[i]
        ans += acc[i] + r
        n = r

    return ans


def solve():
    return count(N)


if __name__ == "__main__":
    print(solve())
