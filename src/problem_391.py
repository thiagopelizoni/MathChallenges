# Problem 391: https://projecteuler.net/problem=391
def M(n, cap=64):
    thr = n + 1
    def base(h):
        if h >= thr:
            return (True, 0)
        return (False, [acc + h if acc + h < thr else 0 for acc in range(thr)])
    F = [base(h) for h in range(cap + 1)]
    m = 0
    while True:
        c0, v0 = F[0]
        if c0:
            return v0
        if v0.count(v0[0]) == len(v0):
            return v0[0]
        m += 1
        H = cap - m
        newF = [None] * (H + 1)
        for h in range(H + 1):
            lc, lv = F[h]
            hc, hv = F[h + 1]
            if hc:
                newF[h] = (True, hv if lc else lv[hv])
            elif lc:
                newF[h] = (True, lv)
            else:
                arr = [lv[hv[acc]] for acc in range(thr)]
                newF[h] = (True, arr[0]) if arr.count(arr[0]) == len(arr) else (False, arr)
        F = newF


def solve():
    return sum(M(n) ** 3 for n in range(1, 1001))


if __name__ == "__main__":
    print(solve())
