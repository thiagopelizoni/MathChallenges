# Problem 21: https://projecteuler.net/problem=21
def solve():
    lim = 10_000
    sums = [0] * lim

    for d in range(1, lim // 2 + 1):
        for n in range(d * 2, lim, d):
            sums[n] += d

    total = 0
    for a in range(1, lim):
        b = sums[a]
        if b != a and b < lim and sums[b] == a:
            total += a

    return total

if __name__ == "__main__":
    print(solve())