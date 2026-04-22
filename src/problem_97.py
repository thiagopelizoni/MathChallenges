# Problem 97: https://projecteuler.net/problem=97

def solve():
    mod = 10**10
    return (28433 * pow(2, 7_830_457, mod) + 1) % mod


if __name__ == "__main__":
    print(solve())
