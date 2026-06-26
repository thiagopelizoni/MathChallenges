# Problem 336: https://projecteuler.net/problem=336

from itertools import product


N = 11
INDEX = 2011


def reverse_suffix(a, i):
    a[i:] = reversed(a[i:])


def maximix(n):
    ranges = [range(i + 1, n - 1) for i in range(n - 2)]
    ans = []

    for js in product(*ranges):
        a = [chr(ord("A") + i) for i in range(n)]
        reverse_suffix(a, n - 2)

        for i in range(n - 3, -1, -1):
            reverse_suffix(a, i)
            reverse_suffix(a, js[i])

        ans.append("".join(a))

    return sorted(ans)


def solve():
    return maximix(N)[INDEX - 1]


if __name__ == "__main__":
    print(solve())
