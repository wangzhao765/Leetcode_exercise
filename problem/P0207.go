package problem

import "fmt"

func canFinish(numCourses int, prerequisites [][]int) bool {
	if len(prerequisites) == 0 {
		return true
	}
	flag := make([]int, numCourses)
	preflag := make([]int, len(prerequisites))
	for i := 0; i < len(prerequisites); i++ {
		flag[prerequisites[i][0]] = 1
		if preflag[i] == 0 && !dfs(prerequisites[i][0], &flag, prerequisites, &preflag) {
			return false
		}
		flag[prerequisites[i][0]] = 0
	}
	return true
}

func dfs(now int, flag *[]int, pre [][]int, preflag *[]int) bool {
	if len(pre) == 0 {
		return true
	}
	for i := 0; i < len(pre); i++ {
		if pre[i][0] == now {
			if (*flag)[pre[i][1]] == 1 {
				return false
			} else {
				(*flag)[pre[i][1]] = 1
				(*preflag)[i] = 1
				if !dfs(pre[i][1], flag, pre, preflag) {
					return false
				}
				(*flag)[pre[i][1]] = 0
			}
		}
	}
	return true
}

func P0207() {
	fmt.Println(canFinish(4, [][]int{{2, 0}, {1, 0}, {3, 1}, {3, 2}, {1, 3}}))
}
