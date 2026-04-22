# Problem 95: https://projecteuler.net/problem=95

LIMIT = 1_000_000


def solve():
    s = [0] * (LIMIT + 1)
    for d in range(1, LIMIT // 2 + 1):
        for n in range(2 * d, LIMIT + 1, d):
            s[n] += d

    done = bytearray(LIMIT + 1)
    best_len = 0
    best = 0

    for start in range(2, LIMIT + 1):
        if done[start]:
            continue

        seen = {}
        path = []
        n = start

        while 0 < n <= LIMIT and not done[n] and n not in seen:
            seen[n] = len(path)
            path.append(n)
            n = s[n]

        if 0 < n <= LIMIT and n in seen:
            cycle = path[seen[n]:]
            m = min(cycle)
            if len(cycle) > best_len or len(cycle) == best_len and m < best:
                best_len = len(cycle)
                best = m

        for n in path:
            done[n] = 1

    return best


if __name__ == "__main__":
    print(solve())
