package problem

import (
	"fmt"
	"sort"
)

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	line := make([]int, 0)
	for i := 0; i < len(matrix); i++ {
		line = append(line, matrix[i][len(matrix[i])-1])
	}
	m := sort.Search(len(line), func(i int) bool {
		return line[i] >= target
	})
	if m >= len(matrix) {
		return false
	}
	result := sort.Search(len(matrix[m]), func(i int) bool {
		return matrix[m][i] >= target
	})
	return matrix[m][result] == target
}

func P0074() {
	fmt.Println(searchMatrix([][]int{
		{1},
	}, 2))
}
