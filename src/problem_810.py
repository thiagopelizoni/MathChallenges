# Problem 810: https://projecteuler.net/problem=810
import numpy as np


def solve(rank=5_000_000):
    if rank == 1:
        return 2

    degree = rank.bit_length()
    while True:
        size = 1 << degree
        prime = np.ones(size, dtype=bool)
        prime[0] = False

        for p in range(3, 1 << (degree // 2 + 1), 2):
            if not prime[p >> 1]:
                continue
            factor_degree = p.bit_length() - 1
            multiples = np.empty(size >> factor_degree, dtype=np.min_scalar_type(size - 1))
            multiples[0] = p >> 1
            for j in range(degree - factor_degree):
                half = 1 << j
                np.bitwise_xor(multiples[:half], p << j, out=multiples[half:2 * half])
            prime[multiples[1:]] = False

        if np.count_nonzero(prime) >= rank - 1:
            index = np.flatnonzero(prime)[rank - 2]
            return 2 * int(index) + 1
        degree += 1


if __name__ == "__main__":
    print(solve())
