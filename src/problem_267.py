# Problem 267: https://projecteuler.net/problem=267

from math import comb, log


N = 1000
TARGET = 10**9


def solve():
    target = log(TARGET)

    for h in range(N // 3 + 1, N + 1):
        f = (3 * h - N) / (2 * N)
        gain = h * log(1 + 2 * f) + (N - h) * log(1 - f)
        if gain >= target:
            wins = sum(comb(N, k) for k in range(h, N + 1))
            return f"{wins / 2**N:.12f}"


if __name__ == "__main__":
    print(solve())
