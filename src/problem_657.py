# Problem 657: https://projecteuler.net/problem=657


def solve(a=10**7, n=10**12):
    mod = 1_000_000_007
    if a == 1:
        return 1

    sign = -1 if a % 2 == 0 else 1
    total = sign * (1 - a * (n + 1)) % mod
    coefficient = a
    previous_inverse = 1

    for j in range(2, a):
        inverse = pow(j, -1, mod)
        coefficient = coefficient * (a - j + 1) * inverse % mod
        geometric = (pow(j, n + 1, mod) - 1) * previous_inverse % mod
        total = (total + sign * coefficient * geometric) % mod
        previous_inverse = inverse
        sign = -sign

    return total


if __name__ == "__main__":
    print(solve())
