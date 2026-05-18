# Problem 232: https://projecteuler.net/problem=232
TARGET = 100


def solve():
    f = [[0.0] * TARGET for _ in range(TARGET)]
    g = [[0.0] * TARGET for _ in range(TARGET)]

    for i in range(TARGET - 1, -1, -1):
        for j in range(TARGET - 1, -1, -1):
            a = 0.0 if i == TARGET - 1 else g[i + 1][j]
            best = 0.0
            t = 1
            gain = 1

            while True:
                q = 2.0 ** -t
                s = 1.0 if j + gain >= TARGET else f[i][j + gain]
                best = max(best, (2 * q * s + (1 - q) * a) / (1 + q))
                if j + gain >= TARGET:
                    break
                t += 1
                gain *= 2

            g[i][j] = best
            f[i][j] = 0.5 * (a + best)

    return f"{f[0][0]:.8f}"


if __name__ == "__main__":
    print(solve())
