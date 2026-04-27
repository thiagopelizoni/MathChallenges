# Problem 135: https://projecteuler.net/problem=135


def solve():
    lim = 1_000_000
    cnt = [0] * lim

    for a in range(1, lim):
        bmax = min(3 * a - 1, (lim - 1) // a)
        b = (-a) % 4 or 4

        while b <= bmax:
            cnt[a * b] += 1
            b += 4

    return sum(c == 10 for c in cnt)


if __name__ == "__main__":
    print(solve())
