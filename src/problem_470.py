# Problem 470: https://projecteuler.net/problem=470

from bisect import bisect_right
from itertools import accumulate, combinations
from math import comb


def ramvok_rewards(faces, max_cost):
    k = len(faces)
    suffix = list(accumulate(reversed(faces), initial=0))[::-1]
    rewards = [float(faces[-1])] + [0.0] * max_cost
    value = 0.0

    while True:
        i = bisect_right(faces, value)
        next_value = (i * value + suffix[i]) / k
        gain = next_value - value
        for cost in range(1, min(max_cost, int(gain)) + 1):
            if cost < gain:
                rewards[cost] += gain - cost
        value = next_value
        if gain <= 1:
            return rewards


def super_ramvok(d, max_cost):
    totals = [[0.0] * (max_cost + 1) for _ in range(d + 1)]

    for k in range(1, d + 1):
        for faces in combinations(range(1, d + 1), k):
            rewards = ramvok_rewards(faces, max_cost)
            for cost, reward in enumerate(rewards):
                totals[k][cost] += reward

    visits = 0.0
    result = [0.0] * (max_cost + 1)
    for k in range(1, d + 1):
        visits += 1 / comb(d - 1, k - 1)
        for cost in range(max_cost + 1):
            result[cost] += visits * totals[k][cost]
    return result


def solve():
    n = 20
    return round(sum(sum(super_ramvok(d, n)) for d in range(4, n + 1)))


if __name__ == "__main__":
    print(solve())
