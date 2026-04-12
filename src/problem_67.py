# Problem 67: https://projecteuler.net/problem=67
import urllib.request

def solve():
    url = "https://projecteuler.net/resources/documents/0067_triangle.txt"
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

    triangle = [[int(x) for x in line.split()] for line in data.strip().split('\n')]

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]

if __name__ == "__main__":
    print(solve())