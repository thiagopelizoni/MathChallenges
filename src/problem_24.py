# Problem 24: https://projecteuler.net/problem=24
from math import factorial

def solve():
    digits = list("0123456789")
    k = 10**6 - 1
    ans = []

    for n in range(len(digits), 0, -1):
        f = factorial(n - 1)
        i, k = divmod(k, f)
        ans.append(digits.pop(i))

    return "".join(ans)

if __name__ == "__main__":
    print(solve())