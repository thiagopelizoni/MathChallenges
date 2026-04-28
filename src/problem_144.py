# Problem 144: https://projecteuler.net/problem=144


def solve():
    x0, y0 = 0.0, 10.1
    x, y = 1.4, -9.6
    hits = 1

    while True:
        dx, dy = x - x0, y - y0
        nx, ny = 4 * x, y
        scale = 2 * (dx * nx + dy * ny) / (nx * nx + ny * ny)
        rx, ry = dx - scale * nx, dy - scale * ny

        t = -2 * (4 * x * rx + y * ry) / (4 * rx * rx + ry * ry)
        x0, y0 = x, y
        x, y = x + t * rx, y + t * ry

        if abs(x) <= 0.01 and y > 0:
            return hits
        hits += 1


if __name__ == "__main__":
    print(solve())
