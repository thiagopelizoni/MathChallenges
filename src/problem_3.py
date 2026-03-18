# Problem 3: https://projecteuler.net/problem=3
def solve():
    n = 600_851_475_143
    ans = 1

    while n % 2 == 0:
        ans = 2
        n //= 2

    p = 3
    while p * p <= n:
        while n % p == 0:
            ans = p
            n //= p
        p += 2

    return n if n > 1 else ans


if __name__ == "__main__":
    print(solve())