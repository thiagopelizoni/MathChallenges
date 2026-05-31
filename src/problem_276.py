# Problem 276: https://projecteuler.net/problem=276

from array import array


LIMIT = 10**7
C = [(s * s + 6) // 12 for s in range(13)]
PC = [0]
PS = [0]

for s in range(1, 13):
    PC.append(PC[-1] + C[s])
    PS.append(PS[-1] + s)


def rounded_square_sum(n):
    q, r = divmod(n, 12)
    return (
        24 * q * (q - 1) * (2 * q - 1)
        + 78 * q * (q - 1)
        + PC[12] * q
        + 12 * r * q * q
        + 2 * q * PS[r]
        + PC[r]
    )


def triangles(n):
    return rounded_square_sum(n // 2) + rounded_square_sum((n + 3) // 2)


def mertens(n):
    mu = array("b", [0]) * (n + 1)
    mu[1] = 1
    comp = bytearray(n + 1)
    primes = []

    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1

        for p in primes:
            v = i * p
            if v > n:
                break
            comp[v] = 1
            if i % p == 0:
                break
            mu[v] = -mu[i]

    pref = array("i", [0]) * (n + 1)
    s = 0
    for i in range(1, n + 1):
        s += mu[i]
        pref[i] = s

    return pref


def solve():
    pref = mertens(LIMIT)
    total = 0
    d = 1

    while d <= LIMIT:
        q = LIMIT // d
        e = LIMIT // q
        total += (pref[e] - pref[d - 1]) * triangles(q)
        d = e + 1

    return total


if __name__ == "__main__":
    print(solve())
