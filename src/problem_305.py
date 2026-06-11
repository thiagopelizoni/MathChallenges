# Problem 305: https://projecteuler.net/problem=305


def ap_count(lo, hi, mod, rem):
    if lo >= hi:
        return 0

    first = lo + (rem - lo) % mod
    if first >= hi:
        return 0

    return (hi - 1 - first) // mod + 1


def fixed_before(x, d, r, s):
    l = len(s)
    if r + l > d or r == 0 and s[0] == "0":
        return 0

    x = min(max(x, 10 ** (d - 1)), 10**d)
    tail = d - r - l
    width = 10**tail
    base = 10 ** (l + tail)
    off = int(s) * width
    plo = 0 if r == 0 else 10 ** (r - 1)
    phi = 10**r - 1

    full_hi = (x - off - width) // base
    total = max(0, min(phi, full_hi) - plo + 1) * width

    p = (x - off) // base
    if plo <= p <= phi:
        start = p * base + off
        end = start + width
        if start < x < end:
            total += x - start

    return total


def fixed_count(lo, hi, d, r, s):
    return fixed_before(hi, d, r, s) - fixed_before(lo, d, r, s)


def match_at(n, r, s):
    t = ""

    while len(t) < r + len(s):
        t += str(n)
        n += 1

    return t[r : r + len(s)] == s


def span_count(lo, hi, d, r, s):
    a = d - r
    if a >= len(s):
        return 0

    pref = s[:a]
    rest = s[a:]
    mod = 10**a
    rem = int(pref)
    total = 0
    trans = 10**d - 1

    if lo <= trans < hi and trans % mod == rem and match_at(trans, r, s):
        total += 1

    hi = min(hi, trans)
    if lo >= hi:
        return total

    b = len(rest)
    if b < d:
        if rest[0] == "0":
            return total

        q = int(rest)
        scale = 10 ** (d - b)
        jlo = max(lo + 1, q * scale)
        jhi = min(hi + 1, (q + 1) * scale)
        total += ap_count(jlo, jhi, mod, rem + 1)
    elif b == d:
        if rest[0] != "0":
            i = int(rest) - 1
            if lo <= i < hi and i % mod == rem:
                total += 1
    else:
        head = rest[:d]
        if head[0] != "0":
            i = int(head) - 1
            if lo <= i < hi and i % mod == rem and match_at(i, r, s):
                total += 1

    return total


def count_before(n, s):
    total = 0

    for d in range(1, len(str(n - 1)) + 1):
        lo = 10 ** (d - 1)
        hi = min(n, 10**d)
        if lo >= hi:
            continue

        for r in range(d):
            if r + len(s) <= d:
                total += fixed_count(lo, hi, d, r, s)
            else:
                total += span_count(lo, hi, d, r, s)

    return total


def first_pos(n):
    d = len(str(n))
    return 1 + sum(9 * 10 ** (k - 1) * k for k in range(1, d)) + (n - 10 ** (d - 1)) * d


def f(n):
    s = str(n)
    lo, hi = 1, 10

    while count_before(hi, s) < n:
        hi *= 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if count_before(mid, s) >= n:
            hi = mid
        else:
            lo = mid

    i = hi - 1
    need = n - count_before(i, s)
    hits = [r for r in range(len(str(i))) if match_at(i, r, s)]

    return first_pos(i) + hits[need - 1]


def solve():
    return sum(f(3**k) for k in range(1, 14))


if __name__ == "__main__":
    print(solve())
