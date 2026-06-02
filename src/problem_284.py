# Problem 284: https://projecteuler.net/problem=284


BASE = 14
LIMIT = 10000
DIGITS = "0123456789abcd"


def to_base(n):
    out = []
    while n:
        n, d = divmod(n, BASE)
        out.append(DIGITS[d])
    return "".join(reversed(out)) or "0"


def solve():
    bpow = BASE
    roots = [7, 8]
    carries = [(r * r - r) // BASE for r in roots]
    sums = roots[:]
    total = 1 + sum(sums)

    for _ in range(2, LIMIT + 1):
        prev = bpow
        for i, r in enumerate(roots):
            d = (-(carries[i] % BASE) * pow((2 * r - 1) % BASE, -1, BASE)) % BASE
            carries[i] = (carries[i] + d * (2 * r - 1) + d * d * bpow) // BASE
            roots[i] = r + d * bpow
            sums[i] += d

        bpow *= BASE
        total += sum(s for r, s in zip(roots, sums) if r >= prev)

    return to_base(total)


if __name__ == "__main__":
    print(solve())
