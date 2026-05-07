# Problem 186: https://projecteuler.net/problem=186
from array import array

USERS = 1_000_000
PM = 524_287
TARGET = 990_000


def lagged_fibonacci():
    buf = [0] * 55
    for k in range(1, 56):
        value = (100003 - 200003 * k + 300007 * k**3) % USERS
        buf[k - 1] = value
        yield value

    k = 56
    while True:
        value = (buf[(k - 25) % 55] + buf[(k - 56) % 55]) % USERS
        buf[(k - 1) % 55] = value
        yield value
        k += 1


def solve():
    parent = array("I", range(USERS))
    size = array("I", [1]) * USERS

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    seq = lagged_fibonacci()
    calls = 0

    while True:
        a = next(seq)
        b = next(seq)
        if a == b:
            continue

        calls += 1
        ra = find(a)
        rb = find(b)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        if size[find(PM)] >= TARGET:
            return calls


if __name__ == "__main__":
    print(solve())
