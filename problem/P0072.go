package problem

import (
	"fmt"
	"math"
)

func minDistance(word1 string, word2 string) int {
	l1 := len(word1)
	l2 := len(word2)
	dis := make([][]int, l1+1)
	for i := 0; i <= l1; i++ {
		dis[i] = make([]int, l2+1)
	}
	for i := 0; i <= l1; i++ {
		for j := 0; j <= l2; j++ {
			switch {
			case i == 0:
				dis[i][j] = j
			case j == 0:
				dis[i][j] = i
			case word1[i-1] == word2[j-1]:
				dis[i][j] = dis[i-1][j-1]
			default:
				dis[i][j] = int(math.Min(math.Min(float64(dis[i-1][j-1]), float64(dis[i][j-1])), float64(dis[i-1][j]))) + 1
			}
		}
	}
	return dis[l1][l2]
}

func P0072() {
	fmt.Println(minDistance("b", "a"))
}
