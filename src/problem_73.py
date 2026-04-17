# Problem 73: https://projecteuler.net/problem=73

def solve():
    limit = 12000
    count = [0] * (limit + 1)
    
    for i in range(1, limit + 1):
        count[i] = (i - 1) // 2 - i // 3
        
    ans = 0
    for i in range(1, limit + 1):
        c = count[i]
        ans += c
        for j in range(i * 2, limit + 1, i):
            count[j] -= c
            
    return ans

if __name__ == "__main__":
    print(solve())
