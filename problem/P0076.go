package problem

import (
	"fmt"
)

func minWindow(s string, t string) string {
	if t == "" {
		return ""
	}
	record := make(map[int]int)
	check := func(record map[int]int) bool {
		for _, i := range record {
			if i > 0 {
				return false
			}
		}
		return true
	}
	for _, c := range t {
		if _, ok := record[int(c)]; ok {
			record[int(c)]++
		} else {
			record[int(c)] = 1
		}
	}
	i1 := 0
	i2 := 0
	min := len(s)
	result := ""
	for i1 < len(s) {
		if _, ok := record[int(s[i1])]; ok {
			record[int(s[i1])]--
		}
		for check(record) && i2 <= i1 {
			if i1-i2+1 <= min {
				result = s[i2 : i1+1]
				min = i1 - i2 + 1
			}
			if _, ok2 := record[int(s[i2])]; ok2 {
				record[int(s[i2])]++
			}
			i2++
		}
		i1++
	}
	return result
}

func P0076() {
	fmt.Println(minWindow("A", "A"))
}
