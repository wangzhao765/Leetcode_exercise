package Problem

import "fmt"

func subarraySum(nums []int, k int) int {
	sumList := make([]int, len(nums))
	sumMap := make(map[int]int)
	sumList[0] = nums[0]
	sumMap[sumList[0]] = 1
	for i:=1;i<len(nums);i++ {
		sumList[i] = sumList[i-1] + nums[i]
		if _,ok := sumMap[sumList[i]]; ok {
			sumMap[sumList[i]]++
		} else {
			sumMap[sumList[i]] = 1
		}
	}
	fmt.Println(sumList)
	fmt.Println(sumMap)
	count := 0
	if v, ok := sumMap[k]; ok {
		count = v
	}
	for i:=0;i<len(sumList)-1;i++ {
		sumMap[sumList[i]]--
		if v, ok := sumMap[sumList[i]+k]; ok {
			count += v
		}
	}
	return count
}

func P0560()  {
	fmt.Println(subarraySum([]int{-1, -1, 1}, 0))
}