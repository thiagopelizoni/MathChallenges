# Problem 35: https://projecteuler.net/problem=35
def solve():
    lim = 1_000_000
    is_prime = [True] * lim
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(lim**0.5) + 1):
        if is_prime[p]:
            for n in range(p * p, lim, p):
                is_prime[n] = False

    total = 0
    allowed = {"1", "3", "7", "9"}

    for n in range(2, lim):
        if not is_prime[n]:
            continue
        if n < 10:
            total += 1
            continue

        s = str(n)
        if set(s) - allowed:
            continue

        if all(is_prime[int(s[i:] + s[:i])] for i in range(len(s))):
            total += 1

    return total

if __name__ == "__main__":
    print(solve())