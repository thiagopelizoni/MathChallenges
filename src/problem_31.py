# Problem 31: https://projecteuler.net/problem=31
def solve():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [0] * 201
    dp[0] = 1

    for coin in coins:
        for total in range(coin, 201):
            dp[total] += dp[total - coin]

    return dp[200]

if __name__ == "__main__":
    print(solve())