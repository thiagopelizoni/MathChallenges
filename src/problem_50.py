# Problem 50: https://projecteuler.net/problem=50
from gmpy2 import is_prime, next_prime

def solve():
    lim = 10**6
    primes = [2]
    p = 2
    while True:
        p = int(next_prime(p))
        if p >= lim:
            break
        primes.append(p)

    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)

    best_len = 0
    ans = 0

    for i in range(len(primes)):
        if prefix[i + best_len + 1] - prefix[i] >= lim:
            break
        for j in range(i + best_len + 1, len(prefix)):
            total = prefix[j] - prefix[i]
            if total >= lim:
                break
            if is_prime(total):
                best_len = j - i
                ans = total

    return ans

if __name__ == "__main__":
    print(solve())