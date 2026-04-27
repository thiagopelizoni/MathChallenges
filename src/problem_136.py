# Problem 136: https://projecteuler.net/problem=136


def solve():
    lim = 50_000_000
    cnt = bytearray(lim)

    for a in range(1, lim):
        bmax = min(3 * a - 1, (lim - 1) // a)
        b = (-a) % 4 or 4
        while b <= bmax:
            n = a * b
            if cnt[n] < 2:
                cnt[n] += 1
            b += 4

    return cnt.count(1)


if __name__ == "__main__":
    print(solve())
