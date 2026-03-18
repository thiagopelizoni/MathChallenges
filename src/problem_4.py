# Problem 4: https://projecteuler.net/problem=4
def solve():
    ans = 0

    for a in range(999, 99, -1):
        if a * 999 <= ans:
            break

        if a % 11 == 0:
            b_start = 999
            step = 1
        else:
            b_start = 990
            step = 11

        for b in range(b_start, a - 1, -step):
            p = a * b
            if p <= ans:
                break
            if str(p) == str(p)[::-1]:
                ans = p
                break

    return ans


if __name__ == "__main__":
    print(solve())