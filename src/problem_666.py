# Problem 666: https://projecteuler.net/problem=666
import numpy as np


def solve():
    k, m = 500, 10
    r = [306]
    while len(r) < k * m:
        r.append(r[-1] ** 2 % 10007)
    q = np.array(r).reshape(k, m) % 5
    i = np.arange(k)[:, None]
    s = np.zeros(k)
    while True:
        a = s[i]
        b = s[2 * i % k]
        c = s[(i * i + 1) % k]
        d = s[(i + 1) % k]
        t = np.select([q == 0, q == 1, q == 2, q == 3, q == 4], [1.0, a * a, b, c**3, a * d])
        new = t.mean(axis=1)
        if np.abs(new - s).max() < 1e-15:
            break
        s = new
    return f"{new[0]:.8f}"


if __name__ == "__main__":
    print(solve())
