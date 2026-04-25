# Problem 120: https://projecteuler.net/problem=120


def solve():
    return sum(a * (a - 1 if a % 2 else a - 2) for a in range(3, 1001))


if __name__ == "__main__":
    print(solve())
