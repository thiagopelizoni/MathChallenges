# Problem 326: https://projecteuler.net/problem=326

N = 10**12
M = 10**6
ALPHA = (-1, 3, 6, 7, 13, 14)
BETA = (0, 1, 2, 2, 5, 5)


def solve():
    cnt = [0] * M

    for r, (a, b) in enumerate(zip(ALPHA, BETA)):
        length = (N - r) // 6 + 1
        q, s = divmod(length, M)

        for t in range(M):
            cnt[(9 * t * t + a * t + b) % M] += q + (t < s)

    return sum(c * (c - 1) // 2 for c in cnt)


if __name__ == "__main__":
    print(solve())
