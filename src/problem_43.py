# Problem 43: https://projecteuler.net/problem=43
def solve():
    parts = [f"{n:03d}" for n in range(17, 1000, 17) if len(set(f"{n:03d}")) == 3]

    for p in (13, 11, 7, 5, 3, 2):
        nxt = []

        for s in parts:
            used = set(s)
            for d in "0123456789":
                if d in used:
                    continue
                if int(d + s[:2]) % p == 0:
                    nxt.append(d + s)

        parts = nxt

    total = 0

    for s in parts:
        for d in "0123456789":
            if d not in s:
                total += int(d + s)

    return total


if __name__ == "__main__":
    print(solve())