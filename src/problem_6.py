# Problem 6: https://projecteuler.net/problem=6
def solve():
    n = 100
    s = n * (n + 1) // 2
    sq = n * (n + 1) * (2 * n + 1) // 6
    return s * s - sq


if __name__ == "__main__":
    print(solve())