# Problem 161: https://projecteuler.net/problem=161
from functools import cache


def tilings(h, w):
    shapes = (
        ((0, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 0), (0, 1), (1, 0)),
        ((0, 0), (0, 1), (1, 1)),
        ((0, 0), (1, 0), (1, 1)),
        ((0, 0), (1, -1), (1, 0)),
    )
    area = h * w

    @cache
    def dp(pos, mask):
        if pos == area:
            return int(mask == 0)
        if mask & 1:
            return dp(pos + 1, mask >> 1)

        r, c = divmod(pos, w)
        total = 0
        for shape in shapes:
            bits = 0
            for dr, dc in shape:
                rr, cc = r + dr, c + dc
                if rr >= h or cc < 0 or cc >= w:
                    break
                bit = 1 << (dr * w + dc)
                if mask & bit:
                    break
                bits |= bit
            else:
                total += dp(pos + 1, (mask | bits) >> 1)
        return total

    return dp(0, 0)


def solve():
    return tilings(12, 9)


if __name__ == "__main__":
    print(solve())
