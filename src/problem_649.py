# Problem 649: https://projecteuler.net/problem=649

from collections import Counter

from sympy import fwht


def solve(n=10_000_019, c=100):
    moves = (2, 3, 5, 7)
    mod = 10**9
    g = []
    seen = {}
    width = max(moves)

    while True:
        x = len(g)
        reachable = {g[x - d] for d in moves if d <= x}
        v = 0
        while v in reachable:
            v += 1
        g.append(v)
        if len(g) >= width:
            state = tuple(g[-width:])
            if state in seen:
                start = seen[state]
                break
            seen[state] = len(g)

    cnt = Counter(g[:min(n, start)])
    if n > start:
        q, r = divmod(n - start, len(g) - start)
        cnt.update({v: q * f for v, f in Counter(g[start:]).items()})
        cnt.update(g[start:start + r])

    counts = [cnt[v] for v in range(max(g) + 1)]
    spectrum = fwht(counts)
    size = len(spectrum)
    losing = sum(pow(int(v), 2 * c, mod * size) for v in spectrum) // size
    ans = (pow(n, 2 * c, mod) - losing) % mod
    return f"{ans:09d}"


if __name__ == "__main__":
    print(solve())
