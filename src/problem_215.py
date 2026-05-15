# Problem 215: https://projecteuler.net/problem=215


def rows(width):
    masks = []

    def gen(pos, mask):
        if pos == width:
            masks.append(mask)
            return

        for brick in (2, 3):
            nxt = pos + brick
            if nxt <= width:
                gen(nxt, mask | (1 << nxt) if nxt < width else mask)

    gen(0, 0)
    return masks


def count(width, height):
    masks = rows(width)
    compat = [
        [j for j, b in enumerate(masks) if a & b == 0]
        for a in masks
    ]
    dp = [1] * len(masks)

    for _ in range(height - 1):
        nxt = [0] * len(masks)
        for i, n in enumerate(dp):
            for j in compat[i]:
                nxt[j] += n
        dp = nxt

    return sum(dp)


def solve():
    return count(32, 10)


if __name__ == "__main__":
    print(solve())
