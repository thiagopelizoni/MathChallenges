# Problem 288: https://projecteuler.net/problem=288


def solve():
    p = 61
    q = 10_000_000
    mod = p**10
    s = 290797
    ans = 0
    coeff = 0

    for n in range(q + 1):
        t = s % p
        if n:
            coeff = (coeff * p + 1) % mod
            ans = (ans + t * coeff) % mod
        s = s * s % 50515093

    return ans


if __name__ == "__main__":
    print(solve())
