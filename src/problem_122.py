# Problem 122: https://projecteuler.net/problem=122

from itertools import count


def min_chain(target):
    if target == 1:
        return 0

    chain = [1]

    def search(left):
        top = chain[-1]
        if top == target:
            return True
        if left == 0 or top << left < target:
            return False

        seen = set()
        for x in reversed(chain):
            nxt = top + x
            if nxt <= target and nxt not in seen:
                seen.add(nxt)
                chain.append(nxt)
                if search(left - 1):
                    return True
                chain.pop()
        return False

    for depth in count(1):
        if search(depth):
            return depth


def solve():
    return sum(min_chain(k) for k in range(1, 201))


if __name__ == "__main__":
    print(solve())
