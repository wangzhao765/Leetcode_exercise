package problem

import (
	"fmt"
)

func longestValidParentheses(s string) int {
	type ele struct {
		ch    byte
		index int
	}
	stack := make([]ele, 0)
	result := make([]int, len(s))
	for i, b := range s {
		switch b {
		case 40:
			stack = append(stack, ele{ch: byte(b), index: i})
		case 41:
			if len(stack) != 0 {
				switch stack[len(stack)-1].ch {
				case 40:
					result[stack[len(stack)-1].index] = 1
					result[i] = 1
					stack = stack[:len(stack)-1]
				case 41:
					stack = make([]ele, 0)
				}
			}
		}
	}
	max := 0
	l := 0
	for _, i := range result {
		if i == 1 {
			l++
		} else {
			if l > max {
				max = l
			}
			l = 0
		}
	}
	if l > max {
		max = l
	}
	return max
}

func P0032() {
	fmt.Println(longestValidParentheses("(()"))
}
