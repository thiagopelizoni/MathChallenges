# Problem 61: https://projecteuler.net/problem=61
from collections import defaultdict


def solve():
    nums = {}
    by_head = {}
    for s in range(3, 9):
        cur = []
        head_map = defaultdict(list)
        n = 1
        while True:
            x = n * ((s - 2) * n - (s - 4)) // 2
            if x >= 10000:
                break
            if x >= 1000 and x % 100 >= 10:
                head = x // 100
                tail = x % 100
                cur.append((x, head, tail))
                head_map[head].append((x, tail))
            n += 1
        nums[s] = cur
        by_head[s] = head_map

    def dfs(first, tail, kinds, used, total):
        if not kinds:
            return total if tail == first else None
        for s in kinds:
            for x, nxt in by_head[s].get(tail, ()):
                if x in used:
                    continue
                ans = dfs(first, nxt, kinds - {s}, used | {x}, total + x)
                if ans is not None:
                    return ans
        return None

    for x, head, tail in nums[8]:
        ans = dfs(head, tail, {3, 4, 5, 6, 7}, {x}, x)
        if ans is not None:
            return ans


if __name__ == "__main__":
    print(solve())
