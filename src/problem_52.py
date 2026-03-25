# Problem 52: https://projecteuler.net/problem=52
def key(n):
    return sorted(str(n))

def solve():
    k = 1
    while True:
        lo = 10 ** (k - 1)
        hi = 10 ** k // 6
        for n in range(lo, hi + 1):
            s = key(n)
            if all(key(m * n) == s for m in range(2, 7)):
                return n
        k += 1

if __name__ == "__main__":
    print(solve())