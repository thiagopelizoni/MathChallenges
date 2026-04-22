# Problem 103: https://projecteuler.net/problem=103

N = 7
PREV = [11, 18, 19, 20, 22, 25]


def ordered(a):
    last = a[-1] if a else 0
    full = a + list(range(last + 1, last + 1 + N - len(a)))

    return all(sum(full[:k + 1]) > sum(full[-k:]) for k in range(1, N // 2 + 1))


def solve():
    b = PREV[len(PREV) // 2]
    best = [b] + [b + x for x in PREV]
    best_sum = sum(best)

    def search(a, sums):
        nonlocal best, best_sum

        if len(a) == N:
            total = sum(a)
            if total < best_sum:
                best = a[:]
                best_sum = total
            return

        start = a[-1] + 1 if a else 1
        rem = N - len(a) - 1
        prefix = sum(a)
        x = start

        while prefix + x + rem * (2 * x + rem + 1) // 2 < best_sum:
            shifted = {s + x for s in sums}
            if not sums & shifted and ordered(a + [x]):
                search(a + [x], sums | shifted)
            x += 1

    search([], {0})
    return "".join(map(str, best))


if __name__ == "__main__":
    print(solve())
