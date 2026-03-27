# Problem 60: https://projecteuler.net/problem=60
from functools import cache
from sympy import isprime, primerange

FILTERS = (7, 11, 13, 17, 19)

def search(lim):
    primes = [p for p in primerange(2, lim) if p not in (2, 5)]
    digits = {p: len(str(p)) for p in primes}
    p10 = {p: 10 ** digits[p] for p in primes}
    mods = {r: [pow(10, k, r) for k in range(max(digits.values()) + 1)] for r in FILTERS}
    best = None

    @cache
    def good(a, b):
        da = digits[a]
        db = digits[b]
        for r in FILTERS:
            if (a * mods[r][db] + b) % r == 0:
                return False
            if (b * mods[r][da] + a) % r == 0:
                return False
        return isprime(a * p10[b] + b) and isprime(b * p10[a] + a)

    def dfs(cand, depth, total):
        nonlocal best
        need = 5 - depth
        if len(cand) < need:
            return
        if need == 1:
            total += cand[0]
            if best is None or total < best:
                best = total
            return
        if best is not None and total + sum(cand[:need]) >= best:
            return
        stop = len(cand) - need + 1
        for i in range(stop):
            p = cand[i]
            if best is not None and total + p >= best:
                break
            nxt = [q for q in cand[i + 1:] if good(p, q)]
            dfs(nxt, depth + 1, total + p)

    for r in (1, 2):
        cand = [3] + [p for p in primes if p > 3 and p % 3 == r]
        dfs(cand, 0, 0)
    return best


def solve():
    lim = 10000
    ans = search(lim)
    while ans is None:
        lim *= 2
        ans = search(lim)
    return search(ans)


if __name__ == "__main__":
    print(solve())
