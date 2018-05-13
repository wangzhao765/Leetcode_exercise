package Problem

import "fmt"

func countSubstrings(s string) int {
	if s=="" {
		return 0
	}
	count := 1
	l := 0
	for i:=1;i<len(s);i++ {
		l = 0
		for i-l>=0 && i+l<len(s) && s[i-l]==s[i+l] {
			count++
			l++
		}
		l = 0
		for i-1-l>=0 && i+l<len(s) && s[i-1-l]==s[i+l] {
			count++
			l++
		}
	}
	return count
}

func P0647()  {
	fmt.Println(countSubstrings("aaa"))
}