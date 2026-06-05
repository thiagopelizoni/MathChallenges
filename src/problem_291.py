# Problem 291: https://projecteuler.net/problem=291

import subprocess
from tempfile import TemporaryDirectory


CPP = r"""
#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

const int64 LIMIT = 5000000000000000LL;

inline int64 value(int64 n) {
    return 2 * n * n + 2 * n + 1;
}

int64 isqrt(int64 n) {
    int64 r = sqrt((long double)n);
    while ((r + 1) <= n / (r + 1)) r++;
    while (r > n / r) r--;
    return r;
}

int64 pow_mod(int64 a, int64 e, int64 mod) {
    int64 r = 1;
    while (e) {
        if (e & 1) r = (__int128)r * a % mod;
        a = (__int128)a * a % mod;
        e >>= 1;
    }
    return r;
}

int sqrt_minus_one(int p) {
    int q = p - 1, s = 0;
    while ((q & 1) == 0) {
        q >>= 1;
        s++;
    }

    int z = 2;
    while (pow_mod(z, (p - 1) / 2, p) != p - 1) z++;

    int64 c = pow_mod(z, q, p);
    int64 x = pow_mod(p - 1, (q + 1) / 2, p);
    int64 t = pow_mod(p - 1, q, p);
    int m = s;

    while (t != 1) {
        int i = 1;
        int64 u = (__int128)t * t % p;
        while (u != 1) {
            u = (__int128)u * u % p;
            i++;
        }

        int64 b = c;
        for (int j = 0; j < m - i - 1; j++) b = (__int128)b * b % p;

        x = (__int128)x * b % p;
        c = (__int128)b * b % p;
        t = (__int128)t * c % p;
        m = i;
    }

    return (int)x;
}

int main() {
    int64 maxn = (isqrt(2 * LIMIT - 1) - 1) / 2;
    while (value(maxn + 1) < LIMIT) maxn++;
    while (value(maxn) >= LIMIT) maxn--;

    int rmax = (int)isqrt(value(maxn));
    vector<unsigned char> prime_comp(rmax + 1, 0);
    vector<int> primes;

    for (int i = 2; i <= rmax; i++) {
        if (prime_comp[i]) continue;

        primes.push_back(i);
        if ((int64)i * i <= rmax) {
            for (int64 j = (int64)i * i; j <= rmax; j += i) prime_comp[j] = 1;
        }
    }

    vector<unsigned char> comp(maxn + 1, 0);
    for (int p : primes) {
        if ((p & 3) != 1) continue;

        int r = sqrt_minus_one(p);
        int64 inv2 = (p + 1) / 2;
        int roots[2] = {
            (int)(((int64)(r + p - 1) * inv2) % p),
            (int)(((int64)(p - r - 1) * inv2) % p)
        };

        for (int root : roots) {
            int64 n = root ? root : p;
            if (value(n) == p) n += p;
            for (; n <= maxn; n += p) comp[n] = 1;
        }
    }

    int64 ans = 0;
    for (int64 n = 1; n <= maxn; n++) ans += !comp[n];

    cout << ans << '\n';
}
"""


def solve():
    with TemporaryDirectory() as d:
        exe = f"{d}/problem_291"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", "-x", "c++", "-", "-o", exe],
            input=CPP,
            text=True,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        return int(subprocess.check_output([exe], text=True))


if __name__ == "__main__":
    print(solve())
