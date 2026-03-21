# Problem 26: https://projecteuler.net/problem=26
def cycle_len(d):
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    if d == 1:
        return 0

    k = 1
    n = 10 % d

    while n != 1:
        n = n * 10 % d
        k += 1

    return k

def solve():
    ans = 0
    best = 0

    for d in range(2, 1000):
        cur = cycle_len(d)
        if cur > best:
            best = cur
            ans = d

    return ans

if __name__ == "__main__":
    print(solve())