# Problem 319: https://projecteuler.net/problem=319

N = 10_000_000_000
MOD = 1_000_000_000
SIEVE_LIMIT = 1_000_000


def mobius_prefix(lim):
    mu = [0] * (lim + 1)
    comp = [False] * (lim + 1)
    primes = []
    mu[1] = 1

    for i in range(2, lim + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1

        for p in primes:
            v = i * p
            if v > lim:
                break
            comp[v] = True
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]

    for i in range(1, lim + 1):
        mu[i] += mu[i - 1]

    return mu


def solve():
    prefix = mobius_prefix(SIEVE_LIMIT)
    cache = {}

    def mertens(n):
        if n <= SIEVE_LIMIT:
            return prefix[n]
        if n in cache:
            return cache[n]

        total = 1
        l = 2
        while l <= n:
            q = n // l
            r = n // q
            total -= (r - l + 1) * mertens(q)
            l = r + 1

        cache[n] = total
        return total

    def geom(m):
        return (
            (pow(3, m + 1, 2 * MOD) - 3) // 2
            - (pow(2, m + 1, MOD) - 2)
        ) % MOD

    ans = 0
    l = 1
    while l <= N:
        q = N // l
        r = N // q
        ans += (mertens(r) - mertens(l - 1)) * geom(q)
        ans %= MOD
        l = r + 1

    return ans


if __name__ == "__main__":
    print(solve())
