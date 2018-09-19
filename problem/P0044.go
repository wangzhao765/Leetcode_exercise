package problem

import (
	"fmt"
)

func isMatch(s string, p string) bool {
	ls := len(s)
	lp := len(p)
	dis := make([][]int, ls+1)
	for i := 0; i <= ls; i++ {
		dis[i] = make([]int, lp+1)
	}
	for i := 0; i <= ls; i++ {
		for j := 0; j <= lp; j++ {
			if i == 0 {
				if j == 0 {
					dis[i][j] = 0
				} else if string(p[j-1]) == "*" {
					dis[i][j] = dis[i][j-1]
				} else {
					dis[i][j] = j
				}
				continue
			}
			if j == 0 {
				if string(s[i-1]) == "*" {
					dis[i][j] = dis[i-1][j]
				} else {
					dis[i][j] = i
				}
				continue
			}
			if string(s[i-1]) == "*" {
				min := ls + lp
				for k := 0; k <= j; k++ {
					if dis[i-1][k] < min {
						min = dis[i-1][k]
					}
				}
				dis[i][j] = min
				continue
			}
			if string(p[j-1]) == "*" {
				min := ls + lp
				for k := 0; k <= i; k++ {
					if dis[k][j-1] < min {
						min = dis[k][j-1]
					}
				}
				dis[i][j] = min
				continue
			}
			if string(s[i-1]) == "?" || string(p[j-1]) == "?" || string(s[i-1]) == string(p[j-1]) {
				dis[i][j] = dis[i-1][j-1]
				continue
			} else {
				dis[i][j] = 1
			}
		}
	}
	return dis[ls][lp] == 0
}

func P0044() {
	fmt.Println(isMatch("", ""))
}
