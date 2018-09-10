package problem

func largestRectangleArea(heights []int) int {
	low := 0
	max := 0
	mmax := 0
	for i := 0; i < len(heights); i++ {
		low = heights[i]
		max = 0
		for j := i; j < len(heights); j++ {
			if heights[j] < low {
				low = heights[j]
			}
			if (j-i+1)*low > max {
				max = (j - i + 1) * low
			}
		}
		if max > mmax {
			mmax = max
		}
	}
	return mmax
}

func P0084() {
	heights := []int{2, 1, 5, 6, 2, 3}
	print(largestRectangleArea(heights))
}
