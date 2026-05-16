# Problem 217: https://projecteuler.net/problem=217


def stats(length, leading, mod):
    cnt = [0] * (9 * length + 1)
    sums = [0] * (9 * length + 1)
    cnt[0] = 1

    for pos in range(length):
        nxt_cnt = [0] * (9 * length + 1)
        nxt_sums = [0] * (9 * length + 1)
        digits = range(1, 10) if leading and pos == 0 else range(10)

        for s, n in enumerate(cnt):
            if not n:
                continue
            total = sums[s]
            for d in digits:
                t = s + d
                nxt_cnt[t] = (nxt_cnt[t] + n) % mod
                nxt_sums[t] = (nxt_sums[t] + 10 * total + n * d) % mod

        cnt, sums = nxt_cnt, nxt_sums

    return cnt, sums


def balanced_sum(k, mod):
    if k == 1:
        return 45

    h = k // 2
    left_cnt, left_sum = stats(h, True, mod)
    right_cnt, right_sum = stats(h, False, mod)
    p = pow(10, h, mod)
    total = 0

    if k % 2 == 0:
        for s in range(len(left_cnt)):
            total += left_sum[s] * right_cnt[s] * p + left_cnt[s] * right_sum[s]
    else:
        for s in range(len(left_cnt)):
            total += (
                10 * left_sum[s] * right_cnt[s] * 10 * p
                + 45 * left_cnt[s] * right_cnt[s] * p
                + 10 * left_cnt[s] * right_sum[s]
            )

    return total % mod


def solve():
    mod = 3**15
    return sum(balanced_sum(k, mod) for k in range(1, 48)) % mod


if __name__ == "__main__":
    print(solve())
