package problem

import (
	"fmt"
)

func uniquePaths(m int, n int) int {
	result := make([][]int, m)
	for i := 0; i < m; i++ {
		result[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		result[0][i] = 1
	}
	for i := 0; i < m; i++ {
		result[i][0] = 1
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			result[i][j] = result[i-1][j] + result[i][j-1]
		}
	}
	return result[m-1][n-1]
}

func P0062() {
	fmt.Println(uniquePaths(3, 7))
}
