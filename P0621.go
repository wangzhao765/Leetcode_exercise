package Problem

import "fmt"

func leastInterval(tasks []byte, n int) int {
	if len(tasks)==0 {
		return 0
	}
	count := make(map[byte]int)
	for _, c := range tasks {
		if _, ok := count[c]; ok {
			count[c]++
		} else {
			count[c]=1
		}
	}
	max := 0
	maxcount :=0
	for _, v := range count {
		if v == max {
			maxcount++
		}
		if v>max {
			max = v
			maxcount = 1
		}
	}
	sum := (max-1)*(n+1) + maxcount
	if sum<len(tasks) {
		sum=len(tasks)
	}
	return sum
}

func P0621()  {
	fmt.Println(leastInterval([]byte{'A','A','A','B','B','B'},2))
}