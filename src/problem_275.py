# Problem 275: https://projecteuler.net/problem=275

import subprocess
from tempfile import TemporaryDirectory


CPP = r"""
#include <bits/stdc++.h>
using namespace std;

const int ORDER = 18;
const int MAXC = 20;
const int W = 2 * MAXC + 1;
const int H = MAXC + 1;
const int MAXCELLS = W * H;
const int DX[4] = {0, 0, -1, 1};
const int DY[4] = {-1, 1, 0, 0};

bool placed[MAXCELLS], excluded_cell[MAXCELLS], in_untried[MAXCELLS];
int cells[32];
long long total = 0, sym = 0;
int n_placed = 0, x_sum = 0, min_x = 0, max_x = 0;

inline int enc(int x, int y) { return y * W + x + MAXC; }
inline int decx(int c) { return c % W - MAXC; }
inline int decy(int c) { return c / W; }

void dfs(int* untried, int usz) {
    if (n_placed == ORDER) {
        if (x_sum == 0) {
            total++;
            bool ok = true;
            for (int i = 0; i < ORDER; i++) {
                int c = cells[i];
                if (!placed[enc(-decx(c), decy(c))]) {
                    ok = false;
                    break;
                }
            }
            if (ok) sym++;
        }
        return;
    }

    int r = ORDER - n_placed;
    if (usz == 0) return;
    if ((long long)x_sum + (long long)r * min_x - (long long)r * (r + 1) / 2 > 0) return;
    if ((long long)x_sum + (long long)r * max_x + (long long)r * (r + 1) / 2 < 0) return;

    int c = untried[0];
    int cx = decx(c), cy = decy(c);

    placed[c] = true;
    in_untried[c] = false;
    cells[n_placed++] = c;
    x_sum += cx;

    int old_min = min_x, old_max = max_x;
    if (n_placed == 1) {
        min_x = max_x = cx;
    } else {
        min_x = min(min_x, cx);
        max_x = max(max_x, cx);
    }

    int added[4], n_added = 0;
    for (int d = 0; d < 4; d++) {
        int nx = cx + DX[d], ny = cy + DY[d];
        if (ny < 1 || ny > MAXC || nx < -MAXC || nx > MAXC) continue;

        int nc = enc(nx, ny);
        if (!placed[nc] && !excluded_cell[nc] && !in_untried[nc]) {
            in_untried[nc] = true;
            added[n_added++] = nc;
        }
    }

    sort(added, added + n_added);
    int next_untried[128], next_sz = 0, ai = 0;
    for (int i = 1; i < usz; i++) {
        while (ai < n_added && added[ai] < untried[i]) next_untried[next_sz++] = added[ai++];
        next_untried[next_sz++] = untried[i];
    }
    while (ai < n_added) next_untried[next_sz++] = added[ai++];

    dfs(next_untried, next_sz);

    min_x = old_min;
    max_x = old_max;
    x_sum -= cx;
    n_placed--;
    placed[c] = false;
    for (int i = 0; i < n_added; i++) in_untried[added[i]] = false;

    excluded_cell[c] = true;
    in_untried[c] = false;
    dfs(untried + 1, usz - 1);
    excluded_cell[c] = false;
    in_untried[c] = true;
}

int main() {
    placed[enc(0, 0)] = true;

    int init[4], isz = 0;
    for (int d = 0; d < 4; d++) {
        int nx = DX[d], ny = DY[d];
        if (ny < 1 || ny > MAXC || nx < -MAXC || nx > MAXC) continue;

        int c = enc(nx, ny);
        init[isz++] = c;
        in_untried[c] = true;
    }

    sort(init, init + isz);
    dfs(init, isz);
    cout << (total + sym) / 2 << '\n';
}
"""


def solve():
    with TemporaryDirectory() as d:
        exe = f"{d}/problem_275"
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
