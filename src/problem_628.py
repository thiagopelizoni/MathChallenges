# Problem 628: https://projecteuler.net/problem=628


def solve(n=10**8):
    mod = 1_008_691_207
    fact = 1
    total = 1
    for k in range(1, n):
        fact = fact * k % mod
        total = (total + fact) % mod
    return ((n - 3) * total + 2) % mod


if __name__ == "__main__":
    print(solve())
