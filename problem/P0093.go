package problem

import (
	"fmt"
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) []string {
	check := func(s string) bool {
		i, err := strconv.Atoi(s)
		if err != nil || i < 0 || i > 255 || (i < 10 && len(s) > 1) || (i < 100 && len(s) > 2) {
			return false
		}
		return true
	}
	result := make([]string, 0)
	for i := 1; i <= 3; i++ {
		for j := 1; j <= 3; j++ {
			for k := 1; k <= 3; k++ {
				if i+j+k > len(s) || len(s)-(i+j+k) > 3 {
					continue
				}
				strs := []string{
					s[0:i],
					s[i : i+j],
					s[i+j : i+j+k],
					s[i+j+k : len(s)],
				}
				if check(strs[0]) && check(strs[1]) && check(strs[2]) && check(strs[3]) {
					result = append(result, strings.Join(strs, "."))
				}
			}
		}
	}
	return result
}

func P0093() {
	fmt.Println(restoreIpAddresses("10111"))
}
