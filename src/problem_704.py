# Problem 704: https://projecteuler.net/problem=704


def solve(n=10**16):
    total = 0
    d = 2
    while d <= n + 1:
        total += n + 2 - d - (n + 1) // d
        d *= 2
    return total


if __name__ == "__main__":
    print(solve())
