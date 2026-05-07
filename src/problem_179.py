# Problem 179: https://projecteuler.net/problem=179
from array import array


def divisor_counts(limit):
    tau = array("H", [0]) * (limit + 1)
    exp = bytearray(limit + 1)
    primes = []
    tau[1] = 1

    for n in range(2, limit + 1):
        if tau[n] == 0:
            tau[n] = 2
            exp[n] = 1
            primes.append(n)

        for p in primes:
            m = n * p
            if m > limit:
                break
            if n % p == 0:
                e = exp[n]
                exp[m] = e + 1
                tau[m] = tau[n] // (e + 1) * (e + 2)
                break
            tau[m] = tau[n] * 2
            exp[m] = 1

    return tau


def solve():
    limit = 10_000_000
    tau = divisor_counts(limit)
    return sum(1 for n in range(2, limit) if tau[n] == tau[n + 1])


if __name__ == "__main__":
    print(solve())
