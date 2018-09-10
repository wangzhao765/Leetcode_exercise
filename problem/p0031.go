package problem

import (
	"fmt"
	"math"
)

func nextPermutation(nums []int) {
	i := len(nums) - 1
	for i > 0 {
		if nums[i] > nums[i-1] {
			break
		}
		i--
	}
	if i == 0 {
		reverse(nums, 0, len(nums)-1)
		return
	}
	i--
	j := i + 1
	index := i
	max := math.MaxInt32
	for j < len(nums) {
		if nums[j] > nums[i] && nums[j] <= max {
			max = nums[j]
			index = j
		}
		j++
	}
	nums[i], nums[index] = nums[index], nums[i]
	fmt.Println(i + 1)
	reverse(nums, i+1, len(nums)-1)
}

func reverse(nums []int, i, j int) {
	for k := i; k <= (i+j)/2; k++ {
		nums[k], nums[i+j-k] = nums[i+j-k], nums[k]
	}
}

func P0031() {
	nums := []int{2, 3, 1, 3, 3}
	nextPermutation(nums)
	fmt.Println(nums)
}
