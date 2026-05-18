# Problem 233: https://projecteuler.net/problem=233
from sympy import factorint, primerange


LIMIT = 10**11
PATTERNS = ((52,), (17, 1), (10, 2), (7, 3), (3, 2, 1))


def bases():
    out = []

    def search(exps, i, used, n):
        if i == len(exps):
            out.append(n)
            return

        e = exps[i]
        lim = int((LIMIT // n) ** (1 / e)) + 2
        for p in primerange(5, lim + 1):
            if p % 4 == 1 and p not in used:
                q = p**e
                if n * q <= LIMIT:
                    search(exps, i + 1, used | {p}, n * q)

    for exps in PATTERNS:
        search(exps, 0, set(), 1)
    return out


def good_prefix(n):
    pref = [0] * (n + 1)
    s = 0
    for k in range(1, n + 1):
        if all(p % 4 != 1 for p in factorint(k)):
            s += k
        pref[k] = s
    return pref


def solve():
    bs = bases()
    pref = good_prefix(max(LIMIT // b for b in bs))
    return sum(b * pref[LIMIT // b] for b in bs)


if __name__ == "__main__":
    print(solve())
