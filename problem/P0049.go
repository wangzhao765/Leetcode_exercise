package problem

import (
	"fmt"
	"sort"
)

func groupAnagrams(strs []string) [][]string {
	smap := make(map[string][]string)
	convertSliceAndSort := func(str string) string {
		strSlice := make([]string, 0)
		for _, c := range str {
			strSlice = append(strSlice, string(c))
		}
		sort.Strings(strSlice)
		result := ""
		for _, c := range strSlice {
			result = result + c
		}
		return result
	}
	for _, str := range strs {
		strSort := convertSliceAndSort(str)
		if _, ok := smap[strSort]; ok {
			smap[strSort] = append(smap[strSort], str)
		} else {
			smap[strSort] = []string{str}
		}
	}
	result := make([][]string, 0)
	for _, str := range smap {
		result = append(result, str)
	}
	return result
}

func P0049() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}
