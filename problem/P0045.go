package problem

func jump(nums []int) int {
	ans := make([]int, len(nums))
	ans[0] = 1
	if len(nums) <= 1 {
		return 0
	}
	for i := 0; i < len(nums); i++ {
		if ans[i] == 0 {
			return 0
		}
		for j := i + 1; j <= i+nums[i] && j < len(nums); j++ {
			if ans[j] > 0 {
				continue
			}
			ans[j] = ans[i] + 1
		}
	}
	return ans[len(nums)-1] - 1
}

func P0045() {
	nums := []int{2, 3, 1, 1, 4}
	println(jump(nums))
}
