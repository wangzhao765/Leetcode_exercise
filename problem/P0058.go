package problem

import "strings"

func lengthOfLastWord(s string) int {
	strs := strings.Split(s, " ")
	if len(strs) == 0 {
		return 0
	} else {
		for i := len(strs) - 1; i >= 0; i-- {
			if len(strs[i]) == 0 {
				continue
			} else {
				return len(strs[i])
			}
		}
		return 0
	}
}

func P0058() {
	println(lengthOfLastWord("   a "))
}
