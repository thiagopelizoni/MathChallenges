# Problem 330: https://projecteuler.net/problem=330

N = 10**9
MOD = 77_777_777
PRIMES = (7, 11, 73, 101, 137)


def e_period(p):
    inv2 = pow(2, -1, p)
    vals = []

    for exp in range(p - 1):
        w = inv2
        total = 0

        for r in range(1, p):
            total = (total + pow(r, exp, p) * w) % p
            w = w * inv2 % p

        vals.append(total)

    return vals


def residue(n, p):
    vals = e_period(p)
    period = p * (p - 1)
    d = 1 % p

    for k in range(1, min(n, period) + 1):
        d = (k * d + vals[k % (p - 1)]) % p

    if n >= period:
        for k in range(1, n % period + 1):
            d = (k * d + vals[k % (p - 1)]) % p

    if n >= p:
        return -d % p

    fact = 1
    for k in range(2, n + 1):
        fact = fact * k % p

    return (fact - d) % p


def crt(residues):
    x = 0
    m = 1

    for p, r in zip(PRIMES, residues):
        t = ((r - x) % p) * pow(m, -1, p) % p
        x += m * t
        m *= p

    return x % m


def solve():
    return crt([residue(N, p) for p in PRIMES])


if __name__ == "__main__":
    print(solve())
