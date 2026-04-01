# Problem 62: https://projecteuler.net/problem=62
def solve():
    groups = {}
    digits = 1
    n = 1
    while True:
        cube = n ** 3
        cur = len(str(cube))
        if cur != digits:
            ans = min((first for cnt, first in groups.values() if cnt == 5), default=None)
            if ans is not None:
                return ans
            groups = {}
            digits = cur
        key = "".join(sorted(str(cube)))
        cnt, first = groups.get(key, (0, cube))
        groups[key] = (cnt + 1, first)
        n += 1


if __name__ == "__main__":
    print(solve())
