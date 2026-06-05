// Problem 291: https://projecteuler.net/problem=291
package main

import (
	"fmt"
	"math"
)

const limit int64 = 5_000_000_000_000_000

func value(n int64) int64 {
	return 2*n*n + 2*n + 1
}

func isqrt(n int64) int64 {
	r := int64(math.Sqrt(float64(n)))
	for (r + 1) <= n/(r+1) {
		r++
	}
	for r > n/r {
		r--
	}
	return r
}

func powMod(a, e, mod int64) int64 {
	r := int64(1)
	for e > 0 {
		if e%2 == 1 {
			r = r * a % mod
		}
		a = a * a % mod
		e /= 2
	}
	return r
}

func sqrtMinusOne(p int) int {
	q := p - 1
	s := 0
	for q%2 == 0 {
		q /= 2
		s++
	}

	z := 2
	for powMod(int64(z), int64((p-1)/2), int64(p)) != int64(p-1) {
		z++
	}

	c := powMod(int64(z), int64(q), int64(p))
	x := powMod(int64(p-1), int64((q+1)/2), int64(p))
	t := powMod(int64(p-1), int64(q), int64(p))
	m := s

	for t != 1 {
		i := 1
		u := t * t % int64(p)
		for u != 1 {
			u = u * u % int64(p)
			i++
		}

		b := c
		for j := 0; j < m-i-1; j++ {
			b = b * b % int64(p)
		}

		x = x * b % int64(p)
		c = b * b % int64(p)
		t = t * c % int64(p)
		m = i
	}

	return int(x)
}

func primesUpTo(n int) []int {
	comp := make([]bool, n+1)
	primes := make([]int, 0, n/20)

	for i := 2; i <= n; i++ {
		if comp[i] {
			continue
		}

		primes = append(primes, i)
		if int64(i)*int64(i) <= int64(n) {
			for j := i * i; j <= n; j += i {
				comp[j] = true
			}
		}
	}

	return primes
}

func solve() int {
	maxn := (isqrt(2*limit-1) - 1) / 2
	for value(maxn+1) < limit {
		maxn++
	}
	for value(maxn) >= limit {
		maxn--
	}

	composite := make([]bool, maxn+1)
	for _, p := range primesUpTo(int(isqrt(value(maxn)))) {
		if p%4 != 1 {
			continue
		}

		r := sqrtMinusOne(p)
		inv2 := int64((p + 1) / 2)
		roots := [2]int64{
			int64(r+p-1) * inv2 % int64(p),
			int64(p-r-1) * inv2 % int64(p),
		}

		for _, root := range roots {
			n := root
			if n == 0 {
				n = int64(p)
			}
			if value(n) == int64(p) {
				n += int64(p)
			}
			for ; n <= maxn; n += int64(p) {
				composite[n] = true
			}
		}
	}

	total := 0
	for n := int64(1); n <= maxn; n++ {
		if !composite[n] {
			total++
		}
	}
	return total
}

func main() {
	fmt.Println(solve())
}
