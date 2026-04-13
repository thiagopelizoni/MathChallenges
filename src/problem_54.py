# Problem 54: https://projecteuler.net/problem=54
from collections import Counter
import urllib.request


VALUES = {c: i for i, c in enumerate("--23456789TJQKA")}


def rank(hand):
	nums = sorted((VALUES[card[0]] for card in hand), reverse=True)
	cnt = Counter(nums)
	groups = sorted(((count, value) for value, count in cnt.items()), reverse=True)
	flush = len({card[1] for card in hand}) == 1
	straight = nums == [14, 5, 4, 3, 2] or all(nums[i] == nums[i + 1] + 1 for i in range(4))
	high = 5 if nums == [14, 5, 4, 3, 2] else nums[0]

	if straight and flush:
		return 8, high
	if groups[0][0] == 4:
		return 7, groups[0][1], groups[1][1]
	if groups[0][0] == 3 and groups[1][0] == 2:
		return 6, groups[0][1], groups[1][1]
	if flush:
		return 5, *nums
	if straight:
		return 4, high
	if groups[0][0] == 3:
		kickers = sorted((value for value, count in cnt.items() if count == 1), reverse=True)
		return 3, groups[0][1], *kickers
	if groups[0][0] == 2 and groups[1][0] == 2:
		pairs = sorted((value for value, count in cnt.items() if count == 2), reverse=True)
		kicker = next(value for value, count in cnt.items() if count == 1)
		return 2, *pairs, kicker
	if groups[0][0] == 2:
		pair = groups[0][1]
		kickers = sorted((value for value, count in cnt.items() if count == 1), reverse=True)
		return 1, pair, *kickers
	return 0, *nums


def solve():
	url = "https://projecteuler.net/resources/documents/0054_poker.txt"
	total = 0
	with urllib.request.urlopen(url) as response:
		for line in response:
			cards = line.decode('utf-8').split()
			if cards:
				total += rank(cards[:5]) > rank(cards[5:])
	return total


if __name__ == "__main__":
	print(solve())
