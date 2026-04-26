# Problem 126: https://projecteuler.net/problem=126

from itertools import count


TARGET = 1000


def layer(x, y, z, k):
    return 2 * (x * y + x * z + y * z) + 4 * (k - 1) * (x + y + z + k - 2)


def counts(lim):
    c = [0] * (lim + 1)

    for x in count(1):
        if layer(x, x, x, 1) > lim:
            break
        for y in count(x):
            if layer(x, y, y, 1) > lim:
                break
            for z in count(y):
                if layer(x, y, z, 1) > lim:
                    break
                for k in count(1):
                    n = layer(x, y, z, k)
                    if n > lim:
                        break
                    c[n] += 1

    return c


def solve():
    lim = 1000
    while True:
        c = counts(lim)
        for n, total in enumerate(c):
            if total == TARGET:
                return n
        lim *= 2


if __name__ == "__main__":
    print(solve())
