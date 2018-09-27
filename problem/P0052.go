package problem

import (
	"fmt"
	"strings"
)

func totalNQueens(n int) int {
	pos := make([]int, 0)
	left := make([]int, 0)
	right := make([]int, 0)
	sum, _ := searchQueen(n, n, pos, left, right)
	return sum
}

func searchQueen(m int, n int, pos []int, left []int, right []int) (int, [][]string) {
	sum := 0
	result := make([][]string, 0)
	if m == 0 {
		re := make([]string, 0)
		for i := 0; i < n; i++ {
			l := strings.Repeat(".", pos[i]) + "Q" + strings.Repeat(".", n-1-pos[i])
			re = append(re, l)
		}
		return 1, [][]string{re}
	}
	for i := 0; i < n; i++ {
		flag := true
		for _, j := range pos {
			if j == i {
				flag = false
				break
			}
		}
		for _, j := range left {
			if j == i+m {
				flag = false
				break
			}
		}
		for _, j := range right {
			if j == i-m {
				flag = false
				break
			}
		}
		if flag {
			pos = append(pos, i)
			left = append(left, i+m)
			right = append(right, i-m)
			su, re := searchQueen(m-1, n, pos, left, right)
			sum += su
			result = append(result, re...)
			pos = pos[:len(pos)-1]
			left = left[:len(left)-1]
			right = right[:len(right)-1]
		}
	}
	return sum, result
}

func P0052() {
	fmt.Println(totalNQueens(8))
}
