package Problem

import "fmt"

func findTargetSumWays(nums []int, S int) int {
	if len(nums)==0 || S>1000{
		return 0
	}
	var record [][]int
	for i:=0;i<len(nums);i++ {
		record = append(record, make([]int, 2010))
	}
	record[0][nums[0]+1000]++
	record[0][-nums[0]+1000]++
	for i:=1;i<len(nums);i++ {
		for j:=0;j<len(record[0]);j++ {
			if j+nums[i]>=0 && j+nums[i]<len(record[0]) {
				record[i][j]+=record[i-1][j+nums[i]]
			}
			if j-nums[i]>=0 && j-nums[i]<len(record[0]) {
				record[i][j]+=record[i-1][j-nums[i]]
			}
		}
	}
	return record[len(nums)-1][S+1000]
}

func P0494()  {
	fmt.Println(findTargetSumWays([]int{0,0,0,0,0,0,0,0,1},1))
}
