# Problem 150: https://projecteuler.net/problem=150


def triangle(rows):
    t = 0
    values = []

    for r in range(rows):
        row = [0]
        for _ in range(r + 1):
            t = (615949 * t + 797807) % 1_048_576
            row.append(row[-1] + t - 524_288)
        values.append(row)

    return values


def solve():
    rows = 1000
    tri = triangle(rows)
    best = 0

    for r in range(rows):
        for c in range(r + 1):
            total = 0
            for h in range(rows - r):
                row = tri[r + h]
                total += row[c + h + 1] - row[c]
                if total < best:
                    best = total

    return best


if __name__ == "__main__":
    print(solve())
