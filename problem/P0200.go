package problem

import "fmt"

func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}
	x := len(grid)
	y := len(grid[0])
	var flag [][]int
	d := [][]int{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}
	for i := 0; i < x; i++ {
		flag = append(flag, make([]int, y))
	}
	a := 0
	b := 0
	count := 0
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			if grid[i][j] == '1' && flag[i][j] == 0 {
				count++
				var queue [][]int
				queue = append(queue, []int{i, j})
				index := 0
				flag[i][j] = count
				for index < len(queue) {
					for k := 0; k < 4; k++ {
						a = queue[index][0] + d[k][0]
						b = queue[index][1] + d[k][1]
						if a >= 0 && a < x && b >= 0 && b < y && grid[a][b] == '1' && flag[a][b] == 0 {
							queue = append(queue, []int{a, b})
							flag[a][b] = count
						}
					}
					index++
				}
			}
		}
	}
	//fmt.Println(flag)
	return count
}

func P0200() {
	fmt.Println(numIslands([][]byte{{'1', '1', '0', '0', '0'}, {'1', '1', '0', '0', '0'}, {'0', '0', '1', '0', '0'}, {'0', '0', '0', '1', '1'}}))
}
