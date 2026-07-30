# Problem 475: https://projecteuler.net/problem=475


def arrangements(n):
    mod = 1_000_000_007
    quartets = 3 * n
    trios = 4 * n
    musicians = 12 * n

    fact = [1] * (musicians + 1)
    for i in range(1, musicians + 1):
        fact[i] = fact[i - 1] * i % mod
    invfact = [1] * (musicians + 1)
    invfact[musicians] = pow(fact[musicians], mod - 2, mod)
    for i in range(musicians, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod

    inv6 = pow(6, mod - 2, mod)
    pow_inv6 = [1] * (trios + 1)
    pow_neg6 = [1] * (quartets + 1)
    pow3 = [1] * (quartets + 1)
    pow8 = [1] * (quartets + 1)
    for i in range(1, trios + 1):
        pow_inv6[i] = pow_inv6[i - 1] * inv6 % mod
    for i in range(1, quartets + 1):
        pow_neg6[i] = pow_neg6[i - 1] * -6 % mod
        pow3[i] = pow3[i - 1] * 3 % mod
        pow8[i] = pow8[i - 1] * 8 % mod

    total = 0
    for a in range(quartets + 1):
        for b in range(quartets - a + 1):
            pairs = a + 2 * b
            for c in range(quartets - a - b + 1):
                singletons = musicians - 2 * pairs - 3 * c
                if singletons < pairs:
                    continue
                remaining_trios = trios - pairs - c
                d = quartets - a - b - c
                coefficient = fact[quartets]
                coefficient = coefficient * invfact[a] % mod
                coefficient = coefficient * invfact[b] % mod
                coefficient = coefficient * invfact[c] % mod
                coefficient = coefficient * invfact[d] % mod
                coefficient = coefficient * pow_neg6[a] % mod
                coefficient = coefficient * pow3[b] % mod
                coefficient = coefficient * pow8[c] % mod
                ways = fact[singletons] * pow_inv6[remaining_trios] % mod
                ways = ways * invfact[remaining_trios] % mod
                total = (total + coefficient * ways) % mod
    return total


def solve():
    return arrangements(50)


if __name__ == "__main__":
    print(solve())
