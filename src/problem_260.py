# Problem 260: https://projecteuler.net/problem=260
import numpy as np


N = 1000


def solve():
    m = N + 1
    axis = np.zeros((m, m), dtype=bool)
    diag2 = np.zeros((m, m), dtype=bool)
    diag3 = np.zeros((m, m), dtype=bool)
    zall = np.arange(m)
    ans = 0

    for x in range(m):
        for y in range(x, m):
            if axis[x, y]:
                continue

            z = zall[y:]
            d = y - x
            bad = (
                axis[x, z]
                | axis[y, z]
                | diag2[z, d]
                | diag2[y, z - x]
                | diag2[x, z - y]
                | diag3[d, z - x]
            )
            ok = np.flatnonzero(~bad)

            if ok.size:
                z = int(z[ok[0]])
                ans += x + y + z
                axis[x, y] = axis[x, z] = axis[y, z] = True
                diag2[z, d] = diag2[y, z - x] = diag2[x, z - y] = True
                diag3[d, z - x] = True

    return ans


if __name__ == "__main__":
    print(solve())
