package problem

import (
	"fmt"
	"math"
)

func permute(nums []int) [][]int {
	index := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		index[i] = i
	}
	flag := true
	ans := make([][]int, 0)
	for flag {
		temp := []int{}
		for i := 0; i < len(nums); i++ {
			temp = append(temp, nums[index[i]])
		}
		ans = append(ans, temp)
		flag = next(index)
	}
	return ans
}

func next(nums []int) bool {
	index := len(nums) - 1
	for index > 0 && nums[index] <= nums[index-1] {
		index--
	}
	if index == 0 {
		return false
	}
	index--
	max := math.MaxInt32
	maxi := index
	for i := index + 1; i < len(nums); i++ {
		if nums[i] <= max && nums[i] > nums[index] {
			max = nums[i]
			maxi = i
		}
	}
	nums[index], nums[maxi] = nums[maxi], nums[index]
	reverse(nums, index+1, len(nums)-1)
	return true
}

// func reverse(nums []int, i, j int) {
// 	for k := i; k <= (i+j)/2; k++ {
// 		nums[k], nums[i+j-k] = nums[i+j-k], nums[k]
// 	}
// }

func P0046() {
	fmt.Println(permute([]int{1, 1, 2}))
}
