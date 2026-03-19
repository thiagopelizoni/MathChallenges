# Problem 14: https://projecteuler.net/problem=14
def solve():
    lim = 1_000_000
    lens = {1: 1}
    best_n = 1
    best_len = 1

    for n in range(2, lim):
        m = n
        seq = []

        while m not in lens:
            seq.append(m)
            if m % 2 == 0:
                m //= 2
            else:
                m = 3 * m + 1

        length = lens[m]
        for k in reversed(seq):
            length += 1
            lens[k] = length

        if lens[n] > best_len:
            best_len = lens[n]
            best_n = n

    return best_n

if __name__ == "__main__":
    print(solve())