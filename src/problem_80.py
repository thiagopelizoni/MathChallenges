# Problem 80: https://projecteuler.net/problem=80

import decimal

def solve():
    decimal.getcontext().prec = 105
    total_sum = 0
    
    squares = {i * i for i in range(1, 11)}
    
    for n in range(1, 101):
        if n in squares:
            continue
            
        s = str(decimal.Decimal(n).sqrt())
        digits = s.replace('.', '')[:100]
        total_sum += sum(int(d) for d in digits)
            
    return total_sum

if __name__ == "__main__":
    print(solve())
