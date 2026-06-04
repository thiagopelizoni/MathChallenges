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


def trim(state):
    state = list(state)
    while state and state[-1] == 0:
        state.pop()
    return tuple(state)


def label(state, i):
    return state[i] if i < len(state) else 0


def with_label(state, i, value):
    state = list(state)
    while len(state) <= i:
        state.append(0)
    state[i] = value
    return trim(state)


def normalize(state):
    seen = {}
    out = []
    last = -1
    for i, x in enumerate(state):
        if x:
            last = i

    for x in state[: last + 1]:
        if x not in seen:
            seen[x] = len(seen)
        out.append(seen[x])

    return trim(out)


def relabel(state, a, b, width):
    state = list(state)
    for i in range(width + 4):
        if label(state, i) == a:
            while len(state) <= i:
                state.append(0)
            state[i] = b
    return trim(state)


def occurrences(state, a, width):
    return sum(label(state, i) == a for i in range(width + 4))


def moves(state, y, edge, final, width):
    colors = (
        label(state, y),
        label(state, y + 1),
        label(state, y + 2),
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

        st = (edge,) + state
        for i, j in enumerate(block):
            if i == j:
                continue

            a = edge if i == 3 else label(st, y + i + 1)
            b = label(st, y + j + 1)
            if not a:
                continue
            if not b or a == b:
                st = None
                break
            st = relabel(st, a, b, width)

        if st is None:
            continue

        cur = label(st, 0)
        st = trim(st[1:])
        old = label(st, y + 1)
        if occurrences(st, old, width) > 1 or old == cur or final:
            st = with_label(st, y + 1, cur)
            if y == width:
                st = (0,) + st
            ans.append(normalize(st))

    return ans


def count(m, n):
    if m > n:
        m, n = n, m

    dp = {(): 1}
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

    return dp.get((), 0)


def solve():
    return count(6, 10)


if __name__ == "__main__":
    print(solve())
