# Problem 333: https://projecteuler.net/problem=333

LIMIT = 1_000_000


def add(one, multi, other_one, other_multi):
    multi = multi | other_multi | (one & other_one)
    one = (one ^ other_one) & ~multi
    return one, multi


def prime_sieve(n):
    prime = bytearray(b"\x01") * n
    prime[0:2] = b"\x00\x00"

    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            prime[p * p : n : p] = b"\x00" * (((n - 1 - p * p) // p) + 1)

    return prime


def unique_sums():
    mask = (1 << (LIMIT + 1)) - 1
    pow3 = []
    x = 1

    while x <= LIMIT:
        pow3.append(x)
        x *= 3

    max_j = len(pow3) - 1
    one = [0] * (max_j + 2)
    multi = [0] * (max_j + 2)
    one[max_j + 1] = 1

    p2 = 1
    while p2 <= LIMIT:
        old_one = one[:]
        old_multi = multi[:]
        new_one = one[:]
        new_multi = multi[:]

        for lim in range(1, max_j + 2):
            so = old_one[lim]
            sm = old_multi[lim]
            if not (so or sm):
                continue

            for j in range(lim):
                w = p2 * pow3[j]
                if w > LIMIT:
                    break

                new_one[j], new_multi[j] = add(
                    new_one[j],
                    new_multi[j],
                    (so << w) & mask,
                    (sm << w) & mask,
                )

        one = new_one
        multi = new_multi
        p2 *= 2

    ans_one = 0
    ans_multi = 0
    for so, sm in zip(one, multi):
        ans_one, ans_multi = add(ans_one, ans_multi, so, sm)

    return ans_one, ans_multi


def solve():
    one, multi = unique_sums()
    prime = prime_sieve(LIMIT)

    return sum(
        q
        for q in range(2, LIMIT)
        if prime[q] and ((one >> q) & 1) and not ((multi >> q) & 1)
    )


if __name__ == "__main__":
    print(solve())
