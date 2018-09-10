package problem

import "fmt"

func maxProduct(nums []int) int {
	positiveRecord := make([]int, len(nums))
	negativeRecord := make([]int, len(nums))
	if len(nums) == 1 {
		return nums[0]
	}
	if nums[0] > 0 {
		positiveRecord[0] = nums[0]
		negativeRecord[0] = 0
	} else {
		positiveRecord[0] = 0
		negativeRecord[0] = nums[0]
	}
	for i := 1; i < len(nums); i++ {
		if nums[i] > 0 {
			positiveRecord[i] = positiveRecord[i-1] * nums[i]
			negativeRecord[i] = negativeRecord[i-1] * nums[i]
			if positiveRecord[i] == 0 {
				positiveRecord[i] = nums[i]
			}
		} else {
			positiveRecord[i] = negativeRecord[i-1] * nums[i]
			negativeRecord[i] = positiveRecord[i-1] * nums[i]
			if negativeRecord[i] == 0 {
				negativeRecord[i] = nums[i]
			}
		}
	}
	max := 0
	for _, i := range positiveRecord {
		if i > max {
			max = i
		}
	}
	return max
}

func P0152() {
	fmt.Println(maxProduct([]int{-2}))
}
