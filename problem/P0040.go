package problem

import "fmt"

func combinationSum2(candidates []int, target int) [][]int {
	type m struct {
		value int
		index int
		list  []int
	}
	c := make([]int, 0)
	cmap := make(map[int]int, 0)
	for _, i := range candidates {
		if _, ok := cmap[i]; ok {
			cmap[i]++
		} else {
			c = append(c, i)
			cmap[i] = 1
		}
	}
	// fmt.Println(c)
	// fmt.Println(cmap)
	que := make([]m, 0)
	result := make([][]int, 0)
	ind := 0
	for i := 0; i <= cmap[c[0]] && i*c[0] <= target; i++ {
		// fmt.Println(i)
		temp := make([]int, 0)
		for j := 1; j <= i; j++ {
			temp = append(temp, c[0])
		}
		que = append(que, m{
			value: target - i*c[0],
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
		if que[ind].index == len(c) {
			ind++
			continue
		}
		for i := 0; i <= cmap[c[que[ind].index]] && i*c[que[ind].index] <= que[ind].value; i++ {
			temp := make([]int, 0)
			for j := 1; j <= i; j++ {
				temp = append(temp, c[que[ind].index])
			}
			t := m{
				value: que[ind].value - i*c[que[ind].index],
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

func P0040() {
	fmt.Println(combinationSum2([]int{14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12}, 27))
}
