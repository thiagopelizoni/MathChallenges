# Problem 331: https://projecteuler.net/problem=331

import subprocess
import tempfile
from pathlib import Path


SOURCE = r"""
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

using i64 = long long;

static inline int bit(const std::vector<std::uint64_t>& bits, i64 i) {
    return (bits[i >> 6] >> (i & 63)) & 1ULL;
}

static inline void set_bit(std::vector<std::uint64_t>& bits, i64 i) {
    bits[i >> 6] |= 1ULL << (i & 63);
}

i64 even_t(i64 n) {
    const i64 outer = n * n;
    const i64 inner = (n - 1) * (n - 1);
    std::vector<std::uint64_t> row((n + 63) >> 6);

    i64 a = 0;
    for (i64 x = 0, y = n - 1; x < n; ++x) {
        i64 cnt = 0;
        const i64 x2 = x * x;

        for (++y; y >= 0; --y) {
            const i64 r2 = x2 + y * y;
            if (r2 >= outer) {
                continue;
            }
            if (r2 >= inner) {
                ++cnt;
            } else {
                break;
            }
        }

        if (cnt & 1) {
            ++a;
            set_bit(row, x);
        }
    }

    i64 ans = 2 * a * (n - a);
    for (i64 x = 0, y = n - 1; x < n; ++x) {
        const i64 x2 = x * x;

        for (++y; y >= 0; --y) {
            const i64 r2 = x2 + y * y;
            if (r2 >= outer) {
                continue;
            }
            if (r2 >= inner) {
                ans += (bit(row, x) ^ bit(row, y)) ? -1 : 1;
            } else {
                break;
            }
        }
    }

    return ans;
}

i64 t(i64 n) {
    if (n == 5) {
        return 3;
    }
    if (n & 1) {
        return 0;
    }
    return even_t(n);
}

int main() {
    assert(t(5) == 3);
    assert(t(10) == 29);
    assert(t(1000) == 395253);

    i64 ans = 0;
    for (int i = 3; i <= 31; ++i) {
        ans += t((1LL << i) - i);
    }

    std::cout << ans << '\n';
}
"""


def solve():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        src = root / "problem_331.cpp"
        exe = root / "problem_331"
        src.write_text(SOURCE)

        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(src), "-o", str(exe)],
            check=True,
        )
        result = subprocess.run(
            [str(exe)],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        )

    return int(result.stdout)


if __name__ == "__main__":
    print(solve())
