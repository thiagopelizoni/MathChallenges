# Problem 334: https://projecteuler.net/problem=334

N = 1500


def beans(n):
    t = 123456

    for _ in range(n):
        if t & 1:
            t = (t // 2) ^ 926252
        else:
            t //= 2

        yield (t % 2**11) + 1


def sum_squares(a, n):
    b = a + n - 1
    return (b * (b + 1) * (2 * b + 1) - (a - 1) * a * (2 * a - 1)) // 6


def final_squares(m, s):
    c = m * (m + 1) // 2
    a = -((c - s) // m)
    k = m * a + c - s

    return sum_squares(a, m + 1) - (a + k) ** 2


def moves(vals):
    m = sum(vals)
    s = sum(i * v for i, v in enumerate(vals))
    q = sum(i * i * v for i, v in enumerate(vals))

    return (final_squares(m, s) - q) // 2


def solve():
    return moves(list(beans(N)))


if __name__ == "__main__":
    print(solve())
