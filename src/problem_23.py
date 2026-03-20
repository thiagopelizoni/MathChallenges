# Problem 23: https://projecteuler.net/problem=23
def solve():
    lim = 28123
    sums = [0] * (lim + 1)

    for d in range(1, lim // 2 + 1):
        for n in range(d * 2, lim + 1, d):
            sums[n] += d

    abundant = [n for n in range(12, lim + 1) if sums[n] > n]
    can = bytearray(lim + 1)

    for i, a in enumerate(abundant):
        for b in abundant[i:]:
            s = a + b
            if s > lim:
                break
            can[s] = 1

    return sum(n for n in range(1, lim + 1) if not can[n])

if __name__ == "__main__":
    print(solve())