package problem

import (
	"fmt"
	"sort"
)

type queue [][]int

func (q queue) Len() int {
	return len(q)
}

func (q queue) Less(i,j int) bool {
	if q[i][0] == q[j][0] {
		return q[i][1] < q[j][1]
	}
	return q[i][0]>q[j][0]
}

func (q queue) Swap(i,j int)  {
	q[i], q[j] = q[j], q[i]
}

func reconstructQueue(people [][]int) [][]int {
	if len(people)==0 {
		return make([][]int,0)
	}
	var q queue
	q = people
	sort.Sort(q)
	ans := make([][]int, 0)
	ans = append(ans, q[0])
	temp := make([][]int,0)
	for i:=1;i<len(q);i++ {
		temp = append([][]int{}, ans[q[i][1]:len(ans)]...)
		ans = append(ans[0:q[i][1]], q[i])
		ans = append(ans, temp...)
	}
	return ans
}

func P0406()  {
	fmt.Println(reconstructQueue([][]int{{7,0},{4,4},{7,1},{5,0},{6,1},{5,2}}))
}
