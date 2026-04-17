# Problem 74: https://projecteuler.net/problem=74

def solve():
    limit = 1000000
    fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    
    chain_len = [0] * 3000000
    ans = 0
    
    for i in range(1, limit):
        if chain_len[i] > 0:
            if chain_len[i] == 60:
                ans += 1
            continue
            
        path = []
        path_idx = {}
        curr = i
        
        while curr not in path_idx and chain_len[curr] == 0:
            path_idx[curr] = len(path)
            path.append(curr)
            
            nxt = 0
            temp = curr
            while temp > 0:
                nxt += fact[temp % 10]
                temp //= 10
            curr = nxt
            
        if chain_len[curr] > 0:
            l = chain_len[curr]
            p_len = len(path)
            for j, val in enumerate(path):
                chain_len[val] = l + p_len - j
        else:
            idx = path_idx[curr]
            p_len = len(path)
            loop_len = p_len - idx
            for j, val in enumerate(path):
                if j < idx:
                    chain_len[val] = p_len - j
                else:
                    chain_len[val] = loop_len
                    
        if chain_len[i] == 60:
            ans += 1
            
    return ans

if __name__ == "__main__":
    print(solve())
