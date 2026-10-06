# Problem 658: https://projecteuler.net/problem=658


def solve(k=10**7, n=10**12):
    mod = 1_000_000_007
    half = pow(2, -1, mod)
    weight = k % 2
    total = weight
    coefficient = 1
    sign = 1 if k % 2 == 0 else -1
    previous_inverse = 0

    for j in range(1, k):
        inverse = pow(j, -1, mod)
        coefficient = coefficient * (k + 2 - j) * inverse % mod
        weight = (weight + 1 + sign * coefficient) * half % mod
        if j == 1:
            geometric = (n + 1) % mod
        else:
            geometric = (pow(j, n + 1, mod) - 1) * previous_inverse % mod
        total = (total + weight * geometric) % mod
        previous_inverse = inverse
        sign = -sign

    return total


if __name__ == "__main__":
    print(solve())
