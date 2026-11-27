# Problem 809: https://projecteuler.net/problem=809


def solve():
    mod = 10**15
    tower = 2 ** (2**2)
    while True:
        next_tower = pow(2, tower + mod, mod)
        if next_tower == tower:
            return (tower - 3) % mod
        tower = next_tower


if __name__ == "__main__":
    print(solve())
