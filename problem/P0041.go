package problem

func firstMissingPositive(nums []int) int {
	temp := 0
	i := 0
	for i < len(nums) {
		if nums[i] != i+1 && nums[i] <= len(nums) && nums[i] > 0 && nums[i] != nums[nums[i]-1] {
			temp = nums[i]
			nums[i] = nums[temp-1]
			nums[temp-1] = temp
		} else {
			i++
		}
	}
	for i, j := range nums {
		if i+1 != j {
			return i + 1
		}
	}
	return len(nums) + 1
}

func P0041() {
	nums := []int{1, 1}
	println(firstMissingPositive(nums))
}
