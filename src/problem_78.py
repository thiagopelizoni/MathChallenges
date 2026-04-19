# Problem 78: https://projecteuler.net/problem=78

def solve():
    mod = 1000000
    p = [1]
    n = 1
    while True:
        p_n = 0
        k = 1
        while True:
            # First term with k
            g1 = k * (3 * k - 1) // 2
            if g1 > n:
                break
            
            # Second term with -k
            g2 = k * (3 * k + 1) // 2
            
            sign = 1 if k % 2 == 1 else -1
            
            p_n += sign * p[n - g1]
            if g2 <= n:
                p_n += sign * p[n - g2]
            
            p_n %= mod
            k += 1
            
        if p_n == 0:
            return n
        
        p.append(p_n)
        n += 1

if __name__ == "__main__":
    print(solve())
