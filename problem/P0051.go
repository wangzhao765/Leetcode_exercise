package problem

import (
	"fmt"
)

func solveNQueens(n int) [][]string {
	pos := make([]int, 0)
	left := make([]int, 0)
	right := make([]int, 0)
	_, result := searchQueen(n, n, pos, left, right)
	return result
}

func P0051() {
	fmt.Println(solveNQueens(4))
}
