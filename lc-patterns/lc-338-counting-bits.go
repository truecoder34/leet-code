package main

import "fmt"

func main() {
	answ := countBits(2)
	fmt.Println("%v", answ)
	answ2 := countBits(5)
	fmt.Println("%v", answ2)
}

func countBits(n int) []int {
	res := make([]int, n+1)

	for i := range res {
		res[i] = 0
	}
	for i := 1; i < n+1; i++ {
		res[i] = res[i>>1] + i%2
	}
	return res
}
