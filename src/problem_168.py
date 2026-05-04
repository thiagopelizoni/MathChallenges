# Problem 168: https://projecteuler.net/problem=168


def solve():
    mod = 100_000
    total = 0

    for length in range(2, 101):
        p = 10 ** (length - 1)
        lo = 10 ** (length - 2)
        for q in range(1, 10):
            den = 10 * q - 1
            for d in range(1, 10):
                num = d * (p - q)
                if num % den == 0:
                    a = num // den
                    if lo <= a < p:
                        total = (total + 10 * a + d) % mod

    return total


if __name__ == "__main__":
    print(solve())
