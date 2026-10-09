# Problem 665: https://projecteuler.net/problem=665
def solve():
    lim = 10**7
    used = set()
    dif = set()
    below = {}
    total = 0
    d = 0
    for n in range(lim // 2 + 1):
        if n in used:
            continue
        while d in dif:
            d += 1
        t = n - d
        while True:
            path = []
            while t in below:
                path.append(t)
                t = below[t]
            for p in path:
                below[p] = t
            m = 2 * n - t
            if m not in used and m - n not in dif and 2 * m - n not in below:
                break
            t -= 1
        used.add(n)
        used.add(m)
        dif.add(m - n)
        below[2 * n - m] = 2 * n - m - 1
        below[2 * m - n] = 2 * m - n - 1
        if n + m <= lim:
            total += n + m
    return total


if __name__ == "__main__":
    print(solve())
