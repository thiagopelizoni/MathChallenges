# Problem 277: https://projecteuler.net/problem=277


LIMIT = 10**15
SEQ = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"


def step(a):
    r = a % 3
    if r == 0:
        return "D", a // 3
    if r == 1:
        return "U", (4 * a + 2) // 3
    return "d", (2 * a - 1) // 3


def trace(a, n):
    out = []
    for _ in range(n):
        ch, a = step(a)
        out.append(ch)
    return "".join(out)


def residue(seq):
    r = 0
    mod = 1

    for i, ch in enumerate(seq, 1):
        for t in range(3):
            cand = r + t * mod
            if trace(cand, i)[-1] == ch:
                r = cand
                break
        mod *= 3

    return r, mod


def solve():
    r, mod = residue(SEQ)
    return r + ((LIMIT + 1 - r + mod - 1) // mod) * mod


if __name__ == "__main__":
    print(solve())
