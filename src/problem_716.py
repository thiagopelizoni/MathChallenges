# Problem 716: https://projecteuler.net/problem=716


def solve(h=10_000, w=20_000):
    mod = 1_000_000_007
    a = pow(2, h, mod)
    b = pow(2, w, mod)
    rows = (h - 2) * a + 2
    cols = (w - 2) * b + 2
    both_rows = (h - 4) * a + 2 * h + 4
    both_cols = (w - 4) * b + 2 * w + 4
    total = h * w * a * b - 2 * rows * cols + both_rows * both_cols
    total += 2 * (a - h - 1) * (b - w - 1)
    total -= (a - 2 * h) * (b - 2 * w)
    return total % mod


if __name__ == "__main__":
    print(solve())
