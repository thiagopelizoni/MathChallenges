# Problem 160: https://projecteuler.net/problem=160
MOD5 = 5**5
MOD2 = 2**5
MOD = 10**5


def unit_prefix():
    prefix = [1] * MOD5
    p = 1
    for n in range(1, MOD5):
        if n % 5:
            p = p * n % MOD5
        prefix[n] = p
    return prefix


PREFIX = unit_prefix()


def factorial_without_fives(n):
    ans = 1
    while n:
        q, r = divmod(n, MOD5)
        ans = ans * PREFIX[r] % MOD5
        if q % 2:
            ans = -ans % MOD5
        n //= 5
    return ans


def five_count(n):
    total = 0
    while n:
        n //= 5
        total += n
    return total


def solve():
    n = 10**12
    r5 = factorial_without_fives(n)
    r5 = r5 * pow(pow(2, -1, MOD5), five_count(n), MOD5) % MOD5
    t = (-r5 * pow(MOD5, -1, MOD2)) % MOD2
    return (r5 + MOD5 * t) % MOD


if __name__ == "__main__":
    print(solve())
