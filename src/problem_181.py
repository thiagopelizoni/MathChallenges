# Problem 181: https://projecteuler.net/problem=181


def grouped_count(black, white):
    dp = [[0] * (white + 1) for _ in range(black + 1)]
    dp[0][0] = 1

    for b in range(black + 1):
        for w in range(white + 1):
            if b == 0 and w == 0:
                continue
            for i in range(b, black + 1):
                row = dp[i]
                prev = dp[i - b]
                for j in range(w, white + 1):
                    row[j] += prev[j - w]

    return dp[black][white]


def solve():
    return grouped_count(60, 40)


if __name__ == "__main__":
    print(solve())
