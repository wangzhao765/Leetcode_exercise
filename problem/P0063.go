package problem

import (
	"fmt"
)

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m := len(obstacleGrid)
	n := len(obstacleGrid[0])
	result := make([][]int, m)
	for i := 0; i < m; i++ {
		result[i] = make([]int, n)
	}
	f := 1
	for i := 0; i < n; i++ {
		if obstacleGrid[0][i] == 1 {
			f = 0
		}
		result[0][i] = f
	}
	f = 1
	for i := 0; i < m; i++ {
		if obstacleGrid[i][0] == 1 {
			f = 0
		}
		result[i][0] = f
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			result[i][j] = (1 - obstacleGrid[i][j]) * ((1-obstacleGrid[i-1][j])*result[i-1][j] + (1-obstacleGrid[i][j-1])*result[i][j-1])
		}
	}
	return result[m-1][n-1]
}

func P0063() {
	fmt.Println(uniquePathsWithObstacles([][]int{{0, 0, 0}, {0, 1, 0}, {1, 0, 0}, {0, 0, 0}}))
}
