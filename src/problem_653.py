# Problem 653: https://projecteuler.net/problem=653


def solve(length=1_000_000_000, n=1_000_001, j=500_001):
    diameter = 20
    r = 6_563_116
    position = 0
    phases = []

    for _ in range(n):
        position += r % 1000 + 1
        phases.append(position if r <= 10_000_000 else -position)
        r = r * r % 32_745_673

    phases.sort()
    return length - diameter * (j - 1) - diameter // 2 - phases[j - 1]


if __name__ == "__main__":
    print(solve())
