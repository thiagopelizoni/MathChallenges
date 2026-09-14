# Problem 612: https://projecteuler.net/problem=612

from math import comb


def solve(digits=18):
    mod = 1000267129
    allow_zero = [0]
    exclude_zero = [0]
    for size in range(1, 11):
        suffixes = sum(size**k for k in range(digits))
        allow_zero.append((size - 1) * suffixes)
        exclude_zero.append(size * suffixes)

    total = 0
    for zero in (0, 1):
        for required in range(1 - zero, 10):
            count = 0
            for omitted in range(required + 1):
                ways = allow_zero[10 - omitted]
                if zero:
                    ways -= exclude_zero[9 - omitted]
                count += (-1) ** omitted * comb(required, omitted) * ways
            sign = (-1) ** (required + zero + 1)
            total += sign * comb(9, required) * comb(count, 2)

    return total % mod


if __name__ == "__main__":
    print(solve())
