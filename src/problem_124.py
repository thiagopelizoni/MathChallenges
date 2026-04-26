# Problem 124: https://projecteuler.net/problem=124


def solve():
    lim = 100_000
    rad = [1] * (lim + 1)

    for p in range(2, lim + 1):
        if rad[p] == 1:
            for n in range(p, lim + 1, p):
                rad[n] *= p

    return sorted(range(1, lim + 1), key=lambda n: (rad[n], n))[9999]


if __name__ == "__main__":
    print(solve())
