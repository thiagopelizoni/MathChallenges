# Problem 159: https://projecteuler.net/problem=159


def solve():
    lim = 1_000_000
    mdrs = [0] + [(n - 1) % 9 + 1 for n in range(1, lim)]

    for a in range(2, lim):
        da = mdrs[a]
        for b in range(2, (lim - 1) // a + 1):
            n = a * b
            s = da + mdrs[b]
            if s > mdrs[n]:
                mdrs[n] = s

    return sum(mdrs[2:])


if __name__ == "__main__":
    print(solve())
