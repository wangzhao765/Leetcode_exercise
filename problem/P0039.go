package problem

import (
	"fmt"
)

func combinationSum(candidates []int, target int) [][]int {
	type m struct {
		value int
		index int
		list  []int
	}
	que := make([]m, 0)
	result := make([][]int, 0)
	ind := 0
	for i := 0; i*candidates[0] <= target; i++ {
		// fmt.Println(i)
		temp := make([]int, 0)
		for j := 1; j <= i; j++ {
			temp = append(temp, candidates[0])
		}
		que = append(que, m{
			value: target - i*candidates[0],
			index: 1,
			list:  temp,
		})
	}
	for ind < len(que) {
		if que[ind].value == 0 {
			result = append(result, que[ind].list)
			ind++
			continue
		}
		if que[ind].index == len(candidates) {
			ind++
			continue
		}
		for i := 0; i*candidates[que[ind].index] <= que[ind].value; i++ {
			temp := make([]int, 0)
			for j := 1; j <= i; j++ {
				temp = append(temp, candidates[que[ind].index])
			}
			t := m{
				value: que[ind].value - i*candidates[que[ind].index],
				index: que[ind].index + 1,
				list:  append([]int{}, append(que[ind].list, temp...)...),
			}
			que = append(que, t)
		}
		ind++
	}
	// fmt.Println(que)
	return result
}

func P0039() {
	fmt.Println(combinationSum([]int{3, 12, 9, 11, 6, 7, 8, 5, 4}, 15))
}
