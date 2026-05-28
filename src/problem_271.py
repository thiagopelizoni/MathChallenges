# Problem 271: https://projecteuler.net/problem=271


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


def roots(p):
    return [x for x in range(1, p) if pow(x, 3, p) == 1]


def solve():
    residues = [0]
    mod = 1

    for p in PRIMES:
        inv = pow(mod, -1, p)
        residues = [
            a + mod * ((b - a) * inv % p)
            for a in residues
            for b in roots(p)
        ]
        mod *= p

    return sum(x for x in residues if x > 1)


if __name__ == "__main__":
    print(solve())
