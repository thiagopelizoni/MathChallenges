# Problem 92: https://projecteuler.net/problem=92

def ends_at_89(n):
    if n == 0:
        return False

    while n not in (1, 89):
        n = sum(int(d) ** 2 for d in str(n))
    return n == 89


def solve():
    counts = [0] * 568
    counts[0] = 1

    for _ in range(7):
        nxt = [0] * 568
        for s, cnt in enumerate(counts):
            if cnt:
                for d in range(10):
                    nxt[s + d * d] += cnt
        counts = nxt

    return sum(cnt for s, cnt in enumerate(counts) if ends_at_89(s))


if __name__ == "__main__":
    print(solve())
