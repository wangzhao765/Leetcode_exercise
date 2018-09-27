package problem

import (
	"fmt"
	"strconv"
)

func numDecodings(s string) int {
	result := make([]int, len(s))
	check := func(s string) int {
		switch {
		case len(s) == 1:
			i, err := strconv.Atoi(s)
			if err != nil || i == 0 {
				return 0
			}
		case len(s) == 2:
			i, err := strconv.Atoi(s)
			if err != nil || i < 10 || i > 26 {
				return 0
			}
		}
		return 1
	}
	result[0] = check(s[0:1])
	if len(s) > 1 {
		result[1] = check(s[0:1])*check(s[1:2]) + check(s[0:2])
	}
	for i := 2; i < len(s); i++ {
		result[i] = check(s[i:i+1])*result[i-1] + check(s[i-1:i+1])*result[i-2]
	}
	return result[len(s)-1]
}

func P0091() {
	fmt.Println(numDecodings("1001"))
}
