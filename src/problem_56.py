# Problem 56: https://projecteuler.net/problem=56
def solve():
    ans = 0
    for a in range(1, 100):
        n = 1
        for _ in range(1, 100):
            n *= a
            ans = max(ans, sum(map(int, str(n))))
    return ans

if __name__ == "__main__":
    print(solve())
