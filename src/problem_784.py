# Problem 784: https://projecteuler.net/problem=784

from sympy.ntheory import sqrt_mod_iter


def solve(limit=2_000_000):
    total = 0
    for k in range(1, (limit - 1) // 2 + 1):
        for root in sqrt_mod_iter(1, k):
            first = 2 * k + 1 + (root - 1) % k
            count = (limit - first) // k + 1
            total += count * ((first * first - 1) // k)
            total += first * count * (count - 1)
            total += k * count * (count - 1) * (2 * count - 1) // 6
    return total


if __name__ == "__main__":
    print(solve())
