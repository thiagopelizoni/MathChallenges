# Problem 242: https://projecteuler.net/problem=242
LIMIT = 10**12


def weighted_prefix(n):
    total = 0
    weight = 1

    while n:
        p = 1
        block = 1
        while p * 2 <= n:
            p *= 2
            block *= 3

        total += weight * block
        weight *= 2
        n -= p

    return total + weight


def solve():
    return weighted_prefix((LIMIT - 1) // 4)


if __name__ == "__main__":
    print(solve())
