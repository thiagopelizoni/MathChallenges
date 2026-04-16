# Problem 70: https://projecteuler.net/problem=70

def solve():
    limit = 10**7
    
    sieve_limit = 5000
    is_prime = [True] * sieve_limit
    primes = []
    
    for p in range(2, sieve_limit):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, sieve_limit, p):
                is_prime[i] = False

    min_ratio = float('inf')
    best_n = 0

    for i in range(len(primes)):
        p = primes[i]
        for j in range(i + 1, len(primes)):
            q = primes[j]
            n = p * q
            if n > limit:
                break
            
            phi = (p - 1) * (q - 1)
            
            if sorted(str(n)) == sorted(str(phi)):
                ratio = n / phi
                if ratio < min_ratio:
                    min_ratio = ratio
                    best_n = n

    return best_n

if __name__ == "__main__":
    print(solve())
