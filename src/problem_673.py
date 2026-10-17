# Problem 673: https://projecteuler.net/problem=673

from collections import Counter
import math
import urllib.request


def load_pairs(url):
    text = urllib.request.urlopen(url, timeout=20).read().decode("utf-8")
    pairs = []
    for line in text.strip().splitlines():
        if line:
            u, v = map(int, line.split(","))
            pairs.append((u, v))
    return pairs


def solve():
    n = 500
    mod = 999999937
    beds = load_pairs("https://projecteuler.net/resources/documents/0673_beds.txt")
    desks = load_pairs("https://projecteuler.net/resources/documents/0673_desks.txt")

    bed = [0] * (n + 1)
    desk = [0] * (n + 1)
    for u, v in beds:
        bed[u] = v
        bed[v] = u
    for u, v in desks:
        desk[u] = v
        desk[v] = u

    seen = [False] * (n + 1)
    counts = Counter()

    for i in range(1, n + 1):
        if seen[i]:
            continue
        stack = [i]
        seen[i] = True
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in (bed[u], desk[u]):
                if w and not seen[w]:
                    seen[w] = True
                    stack.append(w)
        v = len(comp)
        b = sum(1 for u in comp if bed[u]) // 2
        d = sum(1 for u in comp if desk[u]) // 2
        counts[(v, b, d)] += 1

    ans = 1
    for (v, b, d), k in counts.items():
        if b + d == v:
            aut = v
        elif b == d:
            aut = 1
        else:
            aut = 2
        ans = ans * math.factorial(k) * pow(aut, k, mod) % mod

    return ans


if __name__ == "__main__":
    print(solve())
