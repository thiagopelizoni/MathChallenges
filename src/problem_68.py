# Problem 68: https://projecteuler.net/problem=68
from itertools import permutations

def solve():
    ans = ""
    nums = set(range(1, 11))
    
    for p in permutations(range(1, 11), 5):
        if 10 in p or sum(p) % 5 != 0:
            continue
            
        s = (55 + sum(p)) // 5
        ext = [s - p[i] - p[(i + 1) % 5] for i in range(5)]
        
        if set(p) | set(ext) == nums:
            idx = ext.index(min(ext))
            res = "".join(
                f"{ext[(idx + i) % 5]}{p[(idx + i) % 5]}{p[(idx + i + 1) % 5]}"
                for i in range(5)
            )
            if res > ans:
                ans = res
                
    return ans

if __name__ == "__main__":
    print(solve())
