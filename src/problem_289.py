# Problem 289: https://projecteuler.net/problem=289

from collections import defaultdict


MOD = 10**10
PARTITIONS = (
    1111,
    1114,
    1133,
    1134,
    1131,
    1211,
    1214,
    1221,
    1222,
    1224,
    1231,
    1232,
    1233,
    1234,
)


def normalize(s):
    seen = [0] * 16
    nxt = 0
    out = 0
    i = 0

    while s >> (4 * i):
        x = (s >> (4 * i)) & 15
        if not seen[x]:
            seen[x] = nxt + 1
            nxt += 1
        out |= (seen[x] - 1) << (4 * i)
        i += 1

    return out


def relabel(s, a, b, width):
    for i in range(width + 4):
        if (s >> (4 * i)) & 15 == a:
            s ^= (a ^ b) << (4 * i)
    return s


def occurrences(s, a, width):
    total = 0
    for _ in range(width + 4):
        total += (s & 15) == a
        s >>= 4
    return total


def moves(state, y, edge, final, width):
    colors = (
        (state >> (4 * y)) & 15,
        (state >> (4 * (y + 1))) & 15,
        (state >> (4 * (y + 2))) & 15,
        edge,
    )
    ans = []

    for code in PARTITIONS:
        block = (
            code // 1000 - 1,
            (code // 100) % 10 - 1,
            (code // 10) % 10 - 1,
            code % 10 - 1,
        )
        ok = True
        for i, c in enumerate(colors):
            if c:
                continue
            for j in range(4):
                if (colors[j] == 0) != (block[i] == block[j]):
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue

        st = (state << 4) | edge
        for i, j in enumerate(block):
            if i == j:
                continue

            a = edge if i == 3 else (st >> (4 * (y + i + 1))) & 15
            b = (st >> (4 * (y + j + 1))) & 15
            if not a:
                continue
            if not b or a == b:
                st = -1
                break
            st = relabel(st, a, b, width)

        if st == -1:
            continue

        cur = st & 15
        st >>= 4
        old = (st >> (4 * (y + 1))) & 15
        if occurrences(st, old, width) > 1 or old == cur or final:
            st ^= (cur ^ old) << (4 * (y + 1))
            if y == width:
                st <<= 4
            ans.append(normalize(st))

    return ans


def count(m, n):
    if m > n:
        m, n = n, m

    dp = {0: 1}
    cache = {}
    for x in range(n + 1):
        for y in range(m + 1):
            nxt = defaultdict(int)
            edge = 0 if x == n or y == m else 15
            final = x == n and y == m
            for state, ways in dp.items():
                key = (state, y, edge, final)
                step = cache.get(key)
                if step is None:
                    step = moves(state, y, edge, final, m)
                    cache[key] = step
                for state2 in step:
                    nxt[state2] = (nxt[state2] + ways) % MOD
            dp = nxt

    return dp.get(0, 0)


def solve():
    return count(6, 10)


if __name__ == "__main__":
    print(solve())
