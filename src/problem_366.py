# Problem 366: https://projecteuler.net/problem=366

from functools import lru_cache


LIMIT = 10**18
MOD = 10**8

FIBS = [1, 2]
while FIBS[-1] <= LIMIT:
    FIBS.append(FIBS[-1] + FIBS[-2])


def block_len(k):
    return FIBS[k + 1] - FIBS[k]


@lru_cache(maxsize=None)
def block_prefix(k, t):
    if t <= 0:
        return 0
    if k <= 3:
        return t * (t - 1) // 2

    run = (FIBS[k] + 1) // 2
    if t <= run:
        return t * (t - 1) // 2

    tail = block_len(k) - run
    prev = k - 2
    start = block_len(prev) - tail
    return run * (run - 1) // 2 + block_prefix(prev, start + t - run) - block_prefix(prev, start)


def summatory(limit):
    total = 0
    for k in range(len(FIBS) - 1):
        if FIBS[k] > limit:
            break

        end = min(limit, FIBS[k + 1] - 1)
        total += block_prefix(k, end - FIBS[k] + 1)
    return total


def solve():
    return summatory(LIMIT) % MOD


if __name__ == "__main__":
    print(solve())
