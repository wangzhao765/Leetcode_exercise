package problem

import (
	"fmt"
	"math"
)

func minPathSum(grid [][]int) int {
	result := make([][]int, len(grid))
	for i := 0; i < len(grid); i++ {
		result[i] = make([]int, len(grid[0]))
	}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if i == 0 && j == 0 {
				result[0][0] = grid[0][0]
				continue
			}
			up := math.MaxInt32
			if i > 0 {
				up = result[i-1][j]
			}
			left := math.MaxInt32
			if j > 0 {
				left = result[i][j-1]
			}
			result[i][j] = int(math.Min(float64(up), float64(left))) + grid[i][j]
		}
	}
	return result[len(grid)-1][len(grid[0])-1]
}

func P0064() {
	fmt.Println(minPathSum([][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}))
}
