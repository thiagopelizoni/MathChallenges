# Problem 685: https://projecteuler.net/problem=685
from math import comb

MOD = 1_000_000_007


def cnt(l, r):
    if l == 0:
        return 1 if r == 0 else 0
    total = 0
    i = 0
    while i <= l and 10 * i <= r:
        k = r - 10 * i
        total += (-1) ** i * comb(l, i) * comb(k + l - 1, k)
        i += 1
    return total


def f(s, m):
    L = (s + 8) // 9
    while cnt(L, 9 * L - s) < m:
        L += 1
    R = 9 * L - s
    val = pow(10, L, MOD) - 1
    pos, l = 0, L
    while R > 0:
        total = cnt(l, R)
        lo, hi = 0, l
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if total - cnt(l - mid, R) < m:
                lo = mid
            else:
                hi = mid - 1
        m -= total - cnt(l - lo, R)
        pos += lo
        l -= lo
        e = min(9, R)
        while True:
            c = cnt(l - 1, R - e)
            if m <= c:
                break
            m -= c
            e -= 1
        val -= e * pow(10, L - 1 - pos, MOD)
        R -= e
        pos += 1
        l -= 1
    return val % MOD


def solve():
    ans = 0
    for n in range(1, 10001):
        ans += f(n ** 3, n ** 4)
    return ans % MOD


if __name__ == "__main__":
    print(solve())
