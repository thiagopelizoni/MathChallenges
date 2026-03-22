# Problem 37: https://projecteuler.net/problem=37
def solve():
    lim = 1_000_000
    is_prime = [True] * lim
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(lim**0.5) + 1):
        if is_prime[p]:
            for n in range(p * p, lim, p):
                is_prime[n] = False

    total = 0
    found = 0

    for n in range(11, lim):
        if not is_prime[n]:
            continue

        s = str(n)
        if any(not is_prime[int(s[i:])] or not is_prime[int(s[:i])] for i in range(1, len(s))):
            continue

        total += n
        found += 1
        if found == 11:
            return total


if __name__ == "__main__":
    print(solve())