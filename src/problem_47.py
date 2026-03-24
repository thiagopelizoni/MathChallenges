# Problem 47: https://projecteuler.net/problem=47
def solve():
    lim = 200_000
    cnt = [0] * lim

    for p in range(2, lim):
        if cnt[p] == 0:
            for n in range(p, lim, p):
                cnt[n] += 1

    run = 0
    for n in range(2, lim):
        if cnt[n] == 4:
            run += 1
            if run == 4:
                return n - 3
        else:
            run = 0

if __name__ == "__main__":
    print(solve())