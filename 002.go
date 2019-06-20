package main

import "fmt"

func fib() func() int {
	x, y := 0, 1
	return func() int {
		x, y = y, x + y
		return x
	}
}

func main() {
	f := fib()
	total := 0
	for {
		num := f()
		if num > 4000000 {
			break
		}
		if num%2 == 0 {
			total = total + num
		}
	}
	fmt.Println(total)
}
