# Problem 507: https://projecteuler.net/problem=507

MOD = 10_000_000
N = 20_000_000


def shortest_l1(a1, a2, a3, b1, b2, b3):
    while True:
        na = abs(a1) + abs(a2) + abs(a3)
        nb = abs(b1) + abs(b2) + abs(b3)
        if nb < na:
            a1, b1 = b1, a1
            a2, b2 = b2, a2
            a3, b3 = b3, a3
            na, nb = nb, na

        best = nb
        multiple = 0
        if a1 and a2 and a3:
            d1, d2, d3 = abs(a1), abs(a2), abs(a3)
            n1 = b1 if a1 > 0 else -b1
            n2 = b2 if a2 > 0 else -b2
            n3 = b3 if a3 > 0 else -b3
            if n1 * d2 > n2 * d1:
                n1, n2, d1, d2 = n2, n1, d2, d1
            if n2 * d3 > n3 * d2:
                n2, n3, d2, d3 = n3, n2, d3, d2
            if n1 * d2 > n2 * d1:
                n1, n2, d1, d2 = n2, n1, d2, d1
            if 2 * d1 >= d1 + d2 + d3:
                q = n1 // d1
            elif 2 * (d1 + d2) >= d1 + d2 + d3:
                q = n2 // d2
            else:
                q = n3 // d3

            for m in (q, q + 1):
                value = (
                    abs(b1 - m * a1)
                    + abs(b2 - m * a2)
                    + abs(b3 - m * a3)
                )
                if value < best:
                    best = value
                    multiple = m
        else:
            for a, b in ((a1, b1), (a2, b2), (a3, b3)):
                if a == 0:
                    continue
                q = b // a
                for m in (q, q + 1):
                    value = (
                        abs(b1 - m * a1)
                        + abs(b2 - m * a2)
                        + abs(b3 - m * a3)
                    )
                    if value < best:
                        best = value
                        multiple = m

        if best >= nb:
            return na
        if best == 0:
            return 0
        b1 -= multiple * a1
        b2 -= multiple * a2
        b3 -= multiple * a3


def solve(limit=N):
    a, b, c = 1, 0, 0
    block = [0] * 12
    total = 0

    for _ in range(limit):
        for i in range(12):
            block[i] = c
            a, b, c = b, c, a + b + c
            if c >= MOD:
                c -= MOD
                if c >= MOD:
                    c -= MOD

        total += shortest_l1(
            block[0] - block[1],
            block[2] + block[3],
            block[4] * block[5],
            block[6] - block[7],
            block[8] + block[9],
            block[10] * block[11],
        )

    return total


if __name__ == "__main__":
    print(solve())
