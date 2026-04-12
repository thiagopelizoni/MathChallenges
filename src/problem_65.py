# Problem 65: https://projecteuler.net/problem=65

def solve():
    h_prev2, h_prev1 = 0, 1
    
    for i in range(100):
        if i == 0:
            a = 2
        elif i % 3 == 2:
            a = 2 * (i + 1) // 3
        else:
            a = 1
            
        h_curr = a * h_prev1 + h_prev2
        h_prev2, h_prev1 = h_prev1, h_curr
        
    return sum(int(d) for d in str(h_prev1))

if __name__ == "__main__":
    print(solve())
