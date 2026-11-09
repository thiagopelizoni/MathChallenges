# Problem 726: https://projecteuler.net/problem=726


def solve(n=10_000):
    mod = 1_000_000_033
    total = 0
    f = 1
    ratio = 1
    power = 1
    size = 0
    for k in range(1, n + 1):
        power = power * 2 % mod
        ratio = ratio * (power - 1) * pow(2 * k - 1, -1, mod) % mod
        for j in range(size + 1, size + k + 1):
            f = f * j % mod
        size += k
        f = f * ratio % mod
        total = (total + f) % mod
    return total


if __name__ == "__main__":
    print(solve())
