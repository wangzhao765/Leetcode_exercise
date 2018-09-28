package problem

import (
	"fmt"
	"reflect"
	"sort"
)

func isScramble(s1 string, s2 string) bool {
	if s1 == s2 {
		return true
	}
	if len(s1) == 1 && s1 != s2 {
		return false
	}
	check := func(s1, s2 string) bool {
		i1 := make([]int, 0)
		i2 := make([]int, 0)
		for i := 0; i < len(s1); i++ {
			i1 = append(i1, int(s1[i]))
			i2 = append(i2, int(s2[i]))
		}
		sort.Ints(i1)
		sort.Ints(i2)
		return reflect.DeepEqual(i1, i2)
	}
	result := false
	for i := 1; i < len(s1); i++ {
		if check(s1[0:i], s2[0:i]) && check(s1[i:len(s1)], s2[i:len(s2)]) {
			result = result || (isScramble(s1[0:i], s2[0:i]) && isScramble(s1[i:len(s1)], s2[i:len(s2)]))
		}
		if check(s1[0:i], s2[len(s1)-i:len(s1)]) && check(s1[i:len(s1)], s2[0:len(s2)-i]) {
			result = result || (isScramble(s1[0:i], s2[len(s1)-i:len(s1)]) && isScramble(s1[i:len(s1)], s2[0:len(s2)-i]))
		}
	}
	return result
}

func P0087() {
	fmt.Println(isScramble("great", "rgtae"))
}
