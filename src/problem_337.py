# Problem 337: https://projecteuler.net/problem=337

from array import array


N = 20_000_000
MOD = 10**8


def totients(n):
    phi = array("I", range(n + 1))

    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i

    return phi


def solve():
    phi = totients(N)
    size = N // 2 + 1
    bit = array("I", [0]) * (size + 1)
    pref = array("I", [0]) * (size + 1)
    ans = 0

    for n in range(1, N + 1):
        if n < 6:
            if n & 1 == 0:
                pref[n >> 1] = ans
            continue

        k = phi[n] >> 1
        if n == 6:
            dp = 1
        else:
            i = k - 1
            total = 0
            while i:
                total += bit[i]
                if total >= MOD:
                    total -= MOD
                i -= i & -i

            dp = total - pref[k]
            if dp < 0:
                dp += MOD

        ans += dp
        if ans >= MOD:
            ans -= MOD

        if n & 1 == 0:
            pref[n >> 1] = ans

        if dp:
            i = k
            while i <= size:
                v = bit[i] + dp
                if v >= MOD:
                    v -= MOD
                bit[i] = v
                i += i & -i

    return ans


if __name__ == "__main__":
    print(solve())
