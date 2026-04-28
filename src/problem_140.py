# Problem 140: https://projecteuler.net/problem=140

from heapq import heapify, heappop, heappush


def solve():
    heap = [(7, 1), (8, 2), (13, 5), (17, 7), (32, 14), (43, 19)]
    heapify(heap)

    nuggets = []
    while len(nuggets) < 30:
        z, y = heappop(heap)
        if z > 7 and z % 5 == 2:
            nuggets.append((z - 7) // 5)
        heappush(heap, (9 * z + 20 * y, 4 * z + 9 * y))

    return sum(nuggets)


if __name__ == "__main__":
    print(solve())
