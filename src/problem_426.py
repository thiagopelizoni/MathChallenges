# Problem 426: https://projecteuler.net/problem=426

from heapq import heapify, heappop, heappush

import numpy as np


RUNS = 10_000_001


def solve():
    n = RUNS + 1
    lengths = np.empty(n, dtype=np.int64)
    bucket_prev = np.full(n, -1, dtype=np.int32)
    bucket_next = np.full(n, -1, dtype=np.int32)
    heads = {}
    s = 290797
    balls = 0

    for i in range(RUNS):
        value = s % 64 + 1
        lengths[i] = value
        if i % 2 == 0:
            balls += value
        old = heads.get(value, -1)
        bucket_next[i] = old
        if old >= 0:
            bucket_prev[old] = i
        heads[value] = i
        s = s * s % 50515093

    lengths[-1] = balls + 1
    heads[balls + 1] = n - 1
    previous = np.arange(-1, n - 1, dtype=np.int32)
    following = np.arange(1, n + 1, dtype=np.int32)
    following[-1] = -1
    heap = list(heads)
    heapify(heap)
    heap_keys = set(heap)

    def insert(i):
        key = int(lengths[i])
        old = heads.get(key, -1)
        bucket_prev[i] = -1
        bucket_next[i] = old
        if old >= 0:
            bucket_prev[old] = i
        heads[key] = i
        if key not in heap_keys:
            heappush(heap, key)
            heap_keys.add(key)

    def remove(i):
        key = int(lengths[i])
        a = int(bucket_prev[i])
        b = int(bucket_next[i])
        if a >= 0:
            bucket_next[a] = b
        elif b >= 0:
            heads[key] = b
        else:
            del heads[key]
        if b >= 0:
            bucket_prev[b] = a
        bucket_prev[i] = bucket_next[i] = -1

    def link(a, b):
        if a >= 0:
            following[a] = b
        if b >= 0:
            previous[b] = a

    total = 0
    for _ in range((RUNS + 1) // 2):
        while heap[0] not in heads:
            heap_keys.remove(heappop(heap))
        k = heap[0]
        x = heads[k]
        remove(x)
        total += k * k

        if x % 2 == 0:
            y = int(following[x])
            left = int(previous[x])
            right = int(following[y])
            remove(y)
            remaining = int(lengths[y]) - k
            lengths[x] = 0
            if remaining == 0:
                lengths[y] = 0
                link(left, right)
            elif left >= 0:
                remove(left)
                outer = int(previous[left])
                lengths[y] = int(lengths[left]) + remaining
                lengths[left] = 0
                link(outer, y)
                link(y, right)
                insert(y)
            else:
                lengths[y] = 0
                link(-1, right)
        else:
            y = int(previous[x])
            left = int(previous[y])
            right = int(following[x])
            remove(y)
            remaining = int(lengths[y]) - k
            lengths[x] = 0
            if remaining == 0:
                lengths[y] = 0
                link(left, right)
            elif right >= 0:
                remove(right)
                outer = int(following[right])
                lengths[y] = remaining + int(lengths[right])
                lengths[right] = 0
                link(left, y)
                link(y, outer)
                insert(y)
            else:
                lengths[y] = remaining
                link(left, y)
                following[y] = -1
                insert(y)

    return total


if __name__ == "__main__":
    print(solve())
