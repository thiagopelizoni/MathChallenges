# Problem 244: https://projecteuler.net/problem=244
MOD = 100000007
START = ".RBBRRBBRRBBRRBB"
TARGET = ".BRBBRBRRBRBBRBR"


def moves():
    ns = []
    for z in range(16):
        r, c = divmod(z, 4)
        cur = []
        if c < 3:
            cur.append(("L", z + 1))
        if c > 0:
            cur.append(("R", z - 1))
        if r < 3:
            cur.append(("U", z + 4))
        if r > 0:
            cur.append(("D", z - 4))
        ns.append(cur)
    return ns


def slide(s, i, j):
    a = list(s)
    a[i], a[j] = a[j], a[i]
    return "".join(a)


def solve():
    ns = moves()
    seen = {START}
    cur = {START: (1, 0)}

    while cur:
        if TARGET in cur:
            return cur[TARGET][1]

        nxt = {}
        for s, (cnt, checksum) in cur.items():
            z = s.index(".")
            for m, j in ns[z]:
                t = slide(s, z, j)
                if t in seen:
                    continue
                cnt0, checksum0 = nxt.get(t, (0, 0))
                nxt[t] = (
                    cnt0 + cnt,
                    (checksum0 + 243 * checksum + cnt * ord(m)) % MOD,
                )

        seen.update(nxt)
        cur = nxt


if __name__ == "__main__":
    print(solve())
