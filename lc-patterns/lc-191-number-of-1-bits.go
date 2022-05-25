package main

import (
	"fmt"
)

func main() {
	answ := hammingWeight(00000000000000000000000000001011)
	fmt.Println("Answer %d", answ)
	answ2 := hammingWeight(00000000000000000000000010000000)
	fmt.Println("Answer %d", answ2)

}

func hammingWeight(num uint32) int {
	fmt.Println(num)

	var cntr uint32 = 0

	for num > 0 {
		cntr += num & 1
		num >>= 1
	}

	return int(cntr)
}
