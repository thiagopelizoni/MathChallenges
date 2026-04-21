# Problem 88: https://projecteuler.net/problem=88

def solve():
    lim = 12_000
    best = [2 * lim] * (lim + 1)

    def search(start, prod, total, length):
        k = prod - total + length
        if k > lim:
            return
        if k >= 2 and prod < best[k]:
            best[k] = prod

        for f in range(start, 2 * lim // prod + 1):
            search(f, prod * f, total + f, length + 1)

    search(2, 1, 0, 0)
    return sum(set(best[2:]))


if __name__ == "__main__":
    print(solve())
