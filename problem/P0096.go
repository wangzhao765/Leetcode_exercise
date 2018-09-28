package problem

import (
	"fmt"
)

func numTrees(n int) int {
	result := make([]int, n+1)
	result[0] = 1
	result[1] = 1
	for i := 2; i <= n; i++ {
		count := 0
		for j := 0; j < i; j++ {
			count += result[j] * result[i-1-j]
		}
		result[i] = count
	}
	return result[n]
}

func P0096() {
	fmt.Println(numTrees(2))
}
