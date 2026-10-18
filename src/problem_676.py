# Problem 676: https://projecteuler.net/problem=676


def m_sum(n, k, l, mod):
    bits = []
    x = n
    while x > 0:
        bits.append(x % 2)
        x //= 2

    dp = {0: [0, 1, 0, 0]}

    for p in range(len(bits) - 1, -1, -1):
        nb = bits[p]
        w = (2 ** (p % k)) - (2 ** (p % l))
        val = 2**p
        nxt = {}

        for diff, (cf, ct, sf, st) in dp.items():
            for b in (0, 1):
                ndiff = diff + b * w
                add = b * val
                ncf = cf
                nsf = sf + cf * add
                nct = 0
                nst = 0

                if b < nb:
                    ncf += ct
                    nsf += st + ct * add
                elif b == nb:
                    nct += ct
                    nst += st + ct * add

                nsf %= mod
                nst %= mod

                cur = nxt.get(ndiff)
                if cur is None:
                    nxt[ndiff] = [ncf % mod, nct, nsf, nst]
                else:
                    cur[0] = (cur[0] + ncf) % mod
                    cur[1] += nct
                    cur[2] = (cur[2] + nsf) % mod
                    cur[3] = (cur[3] + nst) % mod

        dp = nxt

    res = dp.get(0)
    if res is None:
        return 0
    return (res[2] + res[3]) % mod


def solve():
    n = 10**16
    mod = 10**16
    ans = 0
    for k in range(3, 7):
        for l in range(1, k - 1):
            ans = (ans + m_sum(n, k, l, mod)) % mod
    return ans


if __name__ == "__main__":
    print(solve())
