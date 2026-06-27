# Problem 337: https://projecteuler.net/problem=337

from array import array
from sympy import sieve


N = 20_000_000
MOD = 10**8


def solve():
    phi = array("I", [0])
    phi.extend(sieve.totientrange(1, N + 1))

    base = N // 2 + 2
    tree = array("I", [0]) * (2 * base)
    pref = array("I", [0]) * base
    ans = 0

    for n in range(1, N + 1):
        if n < 6:
            if n % 2 == 0:
                pref[n // 2] = ans
            continue

        k = phi[n] // 2
        if n == 6:
            dp = 1
        else:
            left = base
            right = base + k
            total = 0
            while left < right:
                if left % 2:
                    total += tree[left]
                    if total >= MOD:
                        total -= MOD
                    left += 1

                if right % 2:
                    right -= 1
                    total += tree[right]
                    if total >= MOD:
                        total -= MOD

                left //= 2
                right //= 2

            dp = total - pref[k]
            if dp < 0:
                dp += MOD

        ans += dp
        if ans >= MOD:
            ans -= MOD

        if n % 2 == 0:
            pref[n // 2] = ans

        if dp:
            i = base + k
            while i:
                v = tree[i] + dp
                if v >= MOD:
                    v -= MOD
                tree[i] = v
                i //= 2

    return ans


if __name__ == "__main__":
    print(solve())
