# Problem 1: https://projecteuler.net/problem=1
def solve():
    lim = 1000

    def sum_mult(d):
        m = (lim - 1) // d
        return d * m * (m + 1) // 2

    return sum_mult(3) + sum_mult(5) - sum_mult(15)


if __name__ == "__main__":
    print(solve())
