# Problem 171: https://projecteuler.net/problem=171
MOD = 10**9


def solve():
    lim = 20 * 9**2
    cnt = [0] * (lim + 1)
    total = [0] * (lim + 1)
    cnt[0] = 1

    for _ in range(20):
        next_cnt = [0] * (lim + 1)
        next_total = [0] * (lim + 1)
        for s, c in enumerate(cnt):
            if not c:
                continue
            t = total[s]
            for d in range(10):
                u = s + d * d
                next_cnt[u] = (next_cnt[u] + c) % MOD
                next_total[u] = (next_total[u] + 10 * t + d * c) % MOD
        cnt, total = next_cnt, next_total

    squares = {n * n for n in range(1, 41) if n * n <= lim}
    return sum(total[s] for s in squares) % MOD


if __name__ == "__main__":
    print(solve())
