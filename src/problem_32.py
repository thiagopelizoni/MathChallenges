# Problem 32: https://projecteuler.net/problem=32
def is_pandigital(a, b, p):
    s = f"{a}{b}{p}"
    return len(s) == 9 and "0" not in s and len(set(s)) == 9


def solve():
    products = set()

    for a in range(2, 10):
        for b in range(1234, 9877):
            p = a * b
            if is_pandigital(a, b, p):
                products.add(p)

    for a in range(12, 100):
        for b in range(123, 988):
            p = a * b
            if is_pandigital(a, b, p):
                products.add(p)

    return sum(products)


if __name__ == "__main__":
    print(solve())