# Problem 778: https://projecteuler.net/problem=778

from sympy import GF
from sympy.polys.matrices import DM


def solve(r=234_567, m=765_432):
    base = 10
    mod = 1_000_000_009
    field = GF(mod)
    total = 0

    for i in range(len(str(m))):
        place = base ** i
        cycles, tail = divmod(m + 1, base * place)
        counts = [
            cycles * place + max(0, min(place, tail - d * place))
            for d in range(base)
        ]

        rows = [[0] * base for _ in range(base)]
        for a, row in enumerate(rows):
            for d, count in enumerate(counts):
                row[a * d % base] += count

        transition = DM(rows, field)
        ways = (transition ** r).to_list()[1]
        total += place * sum(d * int(count) for d, count in enumerate(ways))

    return total % mod


if __name__ == "__main__":
    print(solve())
