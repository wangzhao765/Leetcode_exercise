package problem

import "fmt"

func canPartition(nums []int) bool {
	if len(nums)==0 {
		return true
	}
	sum := 0
	for _,v := range nums {
		sum += v
	}
	if sum%2 ==1 {
		return false
	}
	sumMap := make(map[int]bool)
	sumList := make([]int, 0)
	for i:=0;i<len(nums);i++ {
		sumList = make([]int, 0)
		sumList = append(sumList, nums[i])
		for k, _ := range sumMap {
			sumList = append(sumList, k+nums[i])
		}
		for _, v := range sumList {
			if _, ok := sumMap[v]; !ok {
				sumMap[v] = true
			}
		}
		if _, ok:=sumMap[sum/2]; ok {
			return true
		}
	}
	return false
}

func P0416()  {
	fmt.Println(canPartition([]int{1,5,11,5}))
}
