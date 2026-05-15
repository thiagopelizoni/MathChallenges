# Problem 214: https://projecteuler.net/problem=214
import numpy as np


def totients(limit):
    phi = np.arange(limit, dtype=np.uint32)

    for p in range(2, limit):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p

    return phi


def chain_lengths(phi):
    chain = np.zeros(len(phi), dtype=np.uint8)
    chain[1] = 1

    for n in range(2, len(phi)):
        chain[n] = chain[phi[n]] + 1

    return chain


def solve():
    limit = 40_000_000
    target = 25
    phi = totients(limit)
    chain = chain_lengths(phi)
    total = 0
    block = 2_000_000

    for start in range(2, limit, block):
        stop = min(limit, start + block)
        n = np.arange(start, stop, dtype=np.uint32)
        mask = (phi[start:stop] == n - 1) & (chain[start:stop] == target)
        total += int(n[mask].sum())

    return total


if __name__ == "__main__":
    print(solve())
