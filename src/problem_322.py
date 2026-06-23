# Problem 322: https://projecteuler.net/problem=322

M = 10**18
N = 10**12 - 10


def digits(n, b):
    ds = []
    while n:
        ds.append(n % b)
        n //= b
    return ds


def constrained_values(ds, b):
    vals = [0]
    place = 1

    for d in ds:
        vals = [v + c * place for v in vals for c in range(d, b)]
        place *= b

    return vals, place


def count_lucas(p, n, m):
    md = digits(m, p)
    nd = digits(n, p)
    less = 0
    equal = 1

    for pos in range(len(md) - 1, -1, -1):
        lo = nd[pos] if pos < len(nd) else 0
        bound = md[pos]
        less, equal = (
            less * (p - lo) + equal * max(0, bound - lo),
            equal if bound >= lo else 0,
        )

    return less


def digitwise_ge(x, n, b):
    while x or n:
        if x % b < n % b:
            return False
        x //= b
        n //= b
    return True


def count_both(n, m):
    lows, base = constrained_values(digits(n, 5), 5)
    lows = [low for low in lows if low < m]
    max_h = max((m - 1 - low) // base for low in lows)

    mod = 1
    k = 0
    while mod <= max_h:
        mod *= 2
        k += 1

    residues, _ = constrained_values(digits(n, 2)[:k], 2)
    inv = pow(base, -1, mod)
    total = 0

    for low in lows:
        high = (m - 1 - low) // base
        for r in residues:
            h = ((r - low) * inv) % mod
            if h <= high and digitwise_ge(low + base * h, n, 2):
                total += 1

    return total


def solve():
    return M - N - count_lucas(2, N, M) - count_lucas(5, N, M) + count_both(N, M)


if __name__ == "__main__":
    print(solve())
