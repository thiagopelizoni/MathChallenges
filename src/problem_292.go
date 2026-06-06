// Problem 292: https://projecteuler.net/problem=292
package main

import (
	"fmt"
	"math"
	"sort"
)

const limit292 = 120

type vector292 struct {
	x int
	y int
	l int
}

func gcd292(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func isqrt292(n int) int {
	r := int(math.Sqrt(float64(n)))
	for (r+1)*(r+1) <= n {
		r++
	}
	for r*r > n {
		r--
	}
	return r
}

func pack292(x, y, p, c int) int {
	side := 2*limit292 + 1
	return (((p*side)+(x+limit292))*side+(y+limit292))*4 + c
}

func unpack292(k int) (int, int, int, int) {
	side := 2*limit292 + 1
	c := k % 4
	k /= 4
	y := k%side - limit292
	k /= side
	x := k%side - limit292
	p := k / side
	return x, y, p, c
}

func groups292(n int) [][]vector292 {
	byDir := make(map[[2]int][]vector292)

	for x := -n; x <= n; x++ {
		for y := -n; y <= n; y++ {
			if x == 0 && y == 0 {
				continue
			}

			l := isqrt292(x*x + y*y)
			if l*l != x*x+y*y || l > n {
				continue
			}

			g := gcd292(abs292(x), abs292(y))
			key := [2]int{x / g, y / g}
			byDir[key] = append(byDir[key], vector292{x, y, l})
		}
	}

	keys := make([][2]int, 0, len(byDir))
	for key := range byDir {
		keys = append(keys, key)
	}
	sort.Slice(keys, func(i, j int) bool {
		if keys[i][0] != keys[j][0] {
			return keys[i][0] < keys[j][0]
		}
		return keys[i][1] < keys[j][1]
	})

	groups := make([][]vector292, 0, len(keys))
	for _, key := range keys {
		v := byDir[key]
		sort.Slice(v, func(i, j int) bool {
			return v[i].l < v[j].l
		})
		groups = append(groups, v)
	}
	return groups
}

func abs292(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func count292(n int) int64 {
	dp := map[int]int64{pack292(0, 0, 0, 0): 1}

	for _, group := range groups292(n) {
		next := make(map[int]int64, len(dp))
		for k, v := range dp {
			next[k] = v
		}

		for k, ways := range dp {
			sx, sy, p, c := unpack292(k)
			for _, v := range group {
				np := p + v.l
				if np > n {
					continue
				}

				nc := c + 1
				if nc > 3 {
					nc = 3
				}
				next[pack292(sx+v.x, sy+v.y, np, nc)] += ways
			}
		}

		dp = next
	}

	var total int64
	for k, ways := range dp {
		x, y, _, c := unpack292(k)
		if x == 0 && y == 0 && c >= 3 {
			total += ways
		}
	}
	return total
}

func solve() int64 {
	return count292(limit292)
}

func main() {
	fmt.Println(solve())
}
