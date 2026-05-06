# Problem 174: https://projecteuler.net/problem=174


def solve():
    lim = 1_000_000
    ways = [0] * (lim + 1)
    thickness = 1

    while True:
        count = lim // (4 * thickness) - thickness
        if count <= 0:
            break
        for hole in range(1, count + 1):
            ways[4 * thickness * (hole + thickness)] += 1
        thickness += 1

    return sum(1 for n in ways if 1 <= n <= 10)


if __name__ == "__main__":
    print(solve())
