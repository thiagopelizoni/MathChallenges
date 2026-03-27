# Problem 57: https://projecteuler.net/problem=57
def solve():
    ans = 0
    n, d = 3, 2
    for _ in range(1000):
        ans += len(str(n)) > len(str(d))
        n, d = n + 2 * d, n + d
    return ans


if __name__ == "__main__":
    print(solve())
