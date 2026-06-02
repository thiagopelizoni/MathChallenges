# Problem 283: https://projecteuler.net/problem=283

import subprocess
from tempfile import TemporaryDirectory


CPP = r"""
#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

const int KMAX = 1000;
const int MAXV = 16 * KMAX * KMAX;
vector<int> spf;

void add_factor(map<int, int>& f, int n, int mul) {
    while (n > 1) {
        int p = spf[n], e = 0;
        while (n % p == 0) {
            n /= p;
            e++;
        }
        f[p] += mul * e;
    }
}

int main() {
    spf.assign(MAXV + 1, 0);
    for (int i = 2; i <= MAXV; i++) {
        if (spf[i] == 0) {
            spf[i] = i;
            if ((int64)i * i <= MAXV) {
                for (int64 j = (int64)i * i; j <= MAXV; j += i) {
                    if (spf[j] == 0) spf[j] = i;
                }
            }
        }
    }

    int64 ans = 0;
    for (int k = 1; k <= KMAX; k++) {
        int64 n = 4LL * k * k;
        map<int, int> nf;
        add_factor(nf, k, 2);
        nf[2] += 2;

        int xmax = sqrt(3.0 * n);
        while ((int64)(xmax + 1) * (xmax + 1) <= 3 * n) xmax++;
        while ((int64)xmax * xmax > 3 * n) xmax--;

        for (int x = 1; x <= xmax; x++) {
            map<int, int> f = nf;
            add_factor(f, (int)(x * x + n), 1);

            int64 m = n * (x * x + n);
            int64 r = sqrt((long double)m);
            while ((r + 1) * (r + 1) <= m) r++;
            while (r * r > m) r--;

            vector<pair<int, int>> fac(f.begin(), f.end());
            function<void(int, int64)> search = [&](int i, int64 d) {
                if (d > r) return;
                if (i == (int)fac.size()) {
                    int64 e = m / d;
                    if ((d + n) % x || (e + n) % x) return;

                    int64 y = (d + n) / x;
                    int64 z = (e + n) / x;
                    if (x <= y && y <= z) ans += 2 * (x + y + z);
                    return;
                }

                auto [p, e] = fac[i];
                int64 q = 1;
                for (int a = 0; a <= e; a++) {
                    search(i + 1, d * q);
                    q *= p;
                }
            };

            search(0, 1);
        }
    }

    cout << ans << '\n';
}
"""


def solve():
    with TemporaryDirectory() as d:
        exe = f"{d}/problem_283"
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
